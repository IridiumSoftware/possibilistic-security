"""
generate_figures.py — Publication figures for Possibilistic Security paper
Run: python3 generate_figures.py
Output: figures/*.png (300 DPI)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

# Style
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.linewidth': 0.8,
    'figure.facecolor': 'white',
    'savefig.facecolor': 'white',
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.3,
})

BLUE = '#2563EB'
RED = '#DC2626'
GREEN = '#16A34A'
ORANGE = '#EA580C'
GRAY = '#6B7280'
DARK = '#1F2937'
LIGHT = '#F3F4F6'


def fig_rosen_triad():
    """Figure 1: The Rosen Triad {f, Φ, β}"""
    fig, ax = plt.subplots(1, 1, figsize=(5, 4.5))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.2, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Triangle vertices
    cx, cy = 0, 0.15
    r = 1.0
    angles = [90, 210, 330]
    pts = [(cx + r * np.cos(np.radians(a)), cy + r * np.sin(np.radians(a))) for a in angles]

    labels = ['β\nOrganization', 'f\nMetabolism', 'Φ\nRepair']
    colors = [RED, BLUE, GREEN]
    descriptions = ['(phenomenological\nanchor)', '(operational\ntransformation)', '(independent\nwitness)']

    for i, (x, y) in enumerate(pts):
        circle = plt.Circle((x, y), 0.28, color=colors[i], alpha=0.15, linewidth=2, edgecolor=colors[i])
        ax.add_patch(circle)
        ax.text(x, y + 0.05, labels[i], ha='center', va='center', fontsize=11,
                fontweight='bold', color=colors[i])
        # Description outside the triangle, away from title
        if i == 0:  # beta at top — put description to the right, not above
            ax.text(x + 0.65, y + 0.35, descriptions[i], ha='left', va='center', fontsize=8, color=GRAY)
        elif i == 1:  # f at bottom-left
            ax.text(x - 0.45, y - 0.45, descriptions[i], ha='center', va='center', fontsize=8, color=GRAY)
        else:  # Phi at bottom-right
            ax.text(x + 0.45, y - 0.45, descriptions[i], ha='center', va='center', fontsize=8, color=GRAY)

    # Arrows between nodes
    arrow_kw = dict(arrowstyle='->', color=DARK, lw=1.5, connectionstyle='arc3,rad=0.15')
    for i in range(3):
        j = (i + 1) % 3
        x1, y1 = pts[i]
        x2, y2 = pts[j]
        # Shorten arrows
        dx, dy = x2 - x1, y2 - y1
        d = np.sqrt(dx**2 + dy**2)
        shrink = 0.32
        sx1 = x1 + shrink * dx / d
        sy1 = y1 + shrink * dy / d
        sx2 = x2 - shrink * dx / d
        sy2 = y2 - shrink * dy / d
        ax.annotate('', xy=(sx2, sy2), xytext=(sx1, sy1),
                    arrowprops=arrow_kw)

    # Arrow labels
    ax.text(-0.85, 0.85, 'produces Φ', ha='center', fontsize=8, color=GRAY, rotation=55)
    ax.text(0.85, 0.85, 'produces f', ha='center', fontsize=8, color=GRAY, rotation=-55)
    ax.text(0, -0.75, 'produces β', ha='center', fontsize=8, color=GRAY)

    ax.set_title('Rosen Closure Triad', fontsize=14, fontweight='bold', pad=20)
    fig.savefig(OUT / 'fig_rosen_triad.png')
    plt.close()
    print("  ✓ fig_rosen_triad.png")


def fig_obstruction_chain():
    """Figure 2: Obstruction Chain L0-L8"""
    fig, ax = plt.subplots(1, 1, figsize=(6, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, 9.5)
    ax.axis('off')

    layers = [
        ('L0', 'Definitions', 'Threat model, scope'),
        ('L1', 'Physical Binding', 'No physical access → eliminated'),
        ('L2', 'Perimeter', 'No network credentials → eliminated'),
        ('L3', 'Encryption at Rest', 'No boot credentials → eliminated'),
        ('L4', 'Process Isolation', 'Malware, bloatware → eliminated'),
        ('L5', 'Identity Gates', 'Wrong biometric/password → eliminated'),
        ('L6', 'Behavioral Invariants', 'Wrong behavior pattern → eliminated'),
        ('L7', 'Compositional Identity', 'Cross-layer inconsistency → eliminated'),
        ('L8', 'Residual Dynamics', 'Zero-days, social engineering'),
    ]

    for i, (lid, name, desc) in enumerate(layers):
        y = 8.5 - i
        # Funnel width narrows
        width = 9.0 - i * 0.6
        x_left = 5 - width / 2
        color_val = 0.15 + i * 0.08
        color = plt.cm.Blues(color_val)

        rect = patches.FancyBboxPatch((x_left, y - 0.35), width, 0.7,
                                       boxstyle="round,pad=0.05",
                                       facecolor=color, edgecolor=BLUE, linewidth=0.8)
        ax.add_patch(rect)
        ax.text(x_left + 0.3, y, f'{lid}', fontsize=9, fontweight='bold', va='center', color=DARK)
        ax.text(5, y + 0.05, name, fontsize=10, fontweight='bold', va='center', ha='center', color=DARK)
        ax.text(5, y - 0.2, desc, fontsize=7, va='center', ha='center', color=GRAY)

    # Arrow at bottom
    ax.annotate('', xy=(5, -0.3), xytext=(5, 0.3),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
    ax.text(5, -0.45, 'CLOSURE RESIDUE\n(legitimate identity)', ha='center', va='top',
            fontsize=10, fontweight='bold', color=GREEN)

    ax.set_title('Identity Obstruction Chain', fontsize=14, fontweight='bold', pad=15)
    fig.savefig(OUT / 'fig_obstruction_chain.png')
    plt.close()
    print("  ✓ fig_obstruction_chain.png")


def fig_mfa_vs_triadic():
    """Figure 3: MFA vs Triadic Architecture"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    for ax in (ax1, ax2):
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')
        ax.axis('off')

    # LEFT: MFA — all factors pointing at f-position
    ax1.set_title('Multi-Factor Authentication\n(Sub-triadic, Gödel-limited)', fontsize=11, fontweight='bold')
    # Central f node
    c = plt.Circle((0, 0), 0.4, color=BLUE, alpha=0.2, edgecolor=BLUE, linewidth=2)
    ax1.add_patch(c)
    ax1.text(0, 0, 'f', fontsize=16, fontweight='bold', ha='center', va='center', color=BLUE)
    ax1.text(0, -0.55, 'User', fontsize=9, ha='center', color=GRAY)

    factors = ['Password', 'SMS Code', 'Biometric', 'Hardware\nToken', 'Passkey']
    factor_angles = [90, 162, 234, 306, 378 - 360 + 18]
    for i, (label, angle) in enumerate(zip(factors, [90, 162, 234, 306, 18])):
        r = 1.4
        x = r * np.cos(np.radians(angle))
        y = r * np.sin(np.radians(angle))
        c2 = plt.Circle((x, y), 0.3, color=RED, alpha=0.1, edgecolor=RED, linewidth=1)
        ax1.add_patch(c2)
        ax1.text(x, y, label, fontsize=7, ha='center', va='center', color=RED)
        # Arrow to center
        dx, dy = -x, -y
        d = np.sqrt(dx**2 + dy**2)
        ax1.annotate('', xy=(0.42 * (-x/d), 0.42 * (-y/d)),
                     xytext=(x - 0.32 * x/d, y - 0.32 * y/d),
                     arrowprops=dict(arrowstyle='->', color=RED, lw=1))

    ax1.text(0, -1.8, 'All factors at f-position\n(redundant self-certification)',
             ha='center', fontsize=9, color=RED, style='italic')

    # RIGHT: Triadic — three positions in loop
    ax2.set_title('Triadic Possibilistic\n(Closure-based, escapes Gödel)', fontsize=11, fontweight='bold')

    tri_pts = [(0, 1.2), (-1.1, -0.7), (1.1, -0.7)]
    tri_labels = ['β\nInfrastructure', 'f\nSubject', 'Φ\nWitness']
    tri_colors = [RED, BLUE, GREEN]
    tri_desc = ['(compositional\nground)', '(user/device)', '(independent\nexternal)']

    for i, ((x, y), label, col) in enumerate(zip(tri_pts, tri_labels, tri_colors)):
        c3 = plt.Circle((x, y), 0.4, color=col, alpha=0.15, edgecolor=col, linewidth=2)
        ax2.add_patch(c3)
        ax2.text(x, y, label, fontsize=9, fontweight='bold', ha='center', va='center', color=col)

    # Closed loop arrows
    for i in range(3):
        j = (i + 1) % 3
        x1, y1 = tri_pts[i]
        x2, y2 = tri_pts[j]
        dx, dy = x2 - x1, y2 - y1
        d = np.sqrt(dx**2 + dy**2)
        shrink = 0.45
        ax2.annotate('', xy=(x2 - shrink * dx / d, y2 - shrink * dy / d),
                     xytext=(x1 + shrink * dx / d, y1 + shrink * dy / d),
                     arrowprops=dict(arrowstyle='->', color=DARK, lw=1.8,
                                    connectionstyle='arc3,rad=0.12'))

    ax2.text(0, -1.8, 'Closed mutual-witness loop\n(categorical guarantee)',
             ha='center', fontsize=9, color=GREEN, style='italic')

    fig.savefig(OUT / 'fig_mfa_vs_triadic.png')
    plt.close()
    print("  ✓ fig_mfa_vs_triadic.png")


def fig_fractal_hierarchy():
    """Figure 4: Fractal Security Hierarchy"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 7)
    ax.axis('off')

    levels = [
        (0, 5.5, 3.0, 'Ecosystem', '(vendors, users, governments)', '#DBEAFE'),
        (0, 4.0, 2.3, 'Organization', '(company, auditors, regulators)', '#BFDBFE'),
        (0, 2.5, 1.6, 'Team', '(AI model, human, org)', '#93C5FD'),
        (0, 1.0, 0.9, 'Individual', '(user, device, infra)', '#60A5FA'),
    ]

    for cx, cy, size, label, desc, color in levels:
        # Draw triangle
        pts_tri = np.array([
            [cx, cy + size * 0.7],
            [cx - size, cy - size * 0.4],
            [cx + size, cy - size * 0.4],
            [cx, cy + size * 0.7],
        ])
        ax.fill(pts_tri[:, 0], pts_tri[:, 1], color=color, alpha=0.5, edgecolor=BLUE, linewidth=1.5)

        # Nodes at vertices
        for px, py in pts_tri[:3]:
            ax.plot(px, py, 'o', color=BLUE, markersize=6)

        ax.text(cx, cy, label, ha='center', va='center', fontsize=11, fontweight='bold', color=DARK)
        ax.text(cx, cy - 0.3, desc, ha='center', va='center', fontsize=8, color=GRAY)

    ax.set_title('Fractal Security Hierarchy\nTriadic Closure at Every Scale', fontsize=14, fontweight='bold', pad=15)
    fig.savefig(OUT / 'fig_fractal_hierarchy.png')
    plt.close()
    print("  ✓ fig_fractal_hierarchy.png")


def fig_closure_stack():
    """Figure 5: PQC / QKD / Possibilistic Stack"""
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    layers_data = [
        (1, 1.0, 8, 1.5, 'Physics Layer\nQKD', 'Closure-grounded\n(no-cloning ← quantum mechanics ← Rosen closure)', GREEN, '✓'),
        (1, 3.0, 8, 1.5, 'Compute Layer\nPQC', 'NOT closure-grounded\n(computational hardness only — the orphan)', RED, '✗'),
        (1, 5.0, 8, 1.5, 'Identity Layer\nPossibilistic', 'Closure-grounded\n(Rosen triads, cross-sector autopoiesis failure)', GREEN, '✓'),
    ]

    for x, y, w, h, label, desc, color, sym in layers_data:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                                       facecolor=color, alpha=0.1, edgecolor=color, linewidth=2)
        ax.add_patch(rect)
        ax.text(x + 0.5, y + h / 2, f'{sym}', fontsize=18, fontweight='bold', va='center', color=color)
        ax.text(x + 1.3, y + h / 2 + 0.2, label, fontsize=11, fontweight='bold', va='center', color=DARK)
        ax.text(x + 1.3, y + h / 2 - 0.3, desc, fontsize=8, va='center', color=GRAY)

    # Bracket on right
    ax.annotate('', xy=(9.3, 1.0), xytext=(9.3, 6.5),
                arrowprops=dict(arrowstyle='-', color=DARK, lw=1))
    ax.text(9.5, 3.75, 'Security\nStack', ha='left', va='center', fontsize=10, color=DARK, fontweight='bold')

    ax.set_title('The Closure Stack: PQC is the Architectural Orphan', fontsize=13, fontweight='bold', pad=15)
    fig.savefig(OUT / 'fig_closure_stack.png')
    plt.close()
    print("  ✓ fig_closure_stack.png")


def fig_gamma_orthogonality():
    """Figure 6: γ-Orthogonality"""
    fig, ax = plt.subplots(1, 1, figsize=(6, 5))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2.5, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    # L vector (compositional core) — vertical
    ax.annotate('', xy=(0, 2.5), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
    ax.text(0.2, 2.6, 'L (compositional core)', fontsize=11, fontweight='bold', color=GREEN, ha='left')
    ax.text(0.2, 2.2, 'identity-carrying structure', fontsize=8, color=GREEN, ha='left')

    # D_F vector (attack surface) — horizontal
    ax.annotate('', xy=(2.5, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=RED, lw=3))
    ax.text(2.6, 0.2, 'D_F (attack surface)', fontsize=11, fontweight='bold', color=RED)
    ax.text(2.6, -0.2, 'credentials, tokens, APIs', fontsize=8, color=RED)

    # Right angle marker
    ax.plot([0.25, 0.25, 0], [0, 0.25, 0.25], color=DARK, lw=1)

    # Origin
    ax.plot(0, 0, 'o', color=DARK, markersize=8)

    # Equation
    ax.text(0, -1.2, 'Tr(L · D_F) = 0', fontsize=16, ha='center', va='center',
            fontweight='bold', color=DARK,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=LIGHT, edgecolor=GRAY))

    ax.text(0, -2.0, 'The attack surface cannot reach the closure.\nYou can attack credentials all day;\nyou cannot attack the closure through them.',
            ha='center', fontsize=9, color=GRAY, style='italic')

    ax.set_title('γ-Orthogonality: Core ⊥ Attack Surface', fontsize=14, fontweight='bold', pad=15)
    fig.savefig(OUT / 'fig_gamma_orthogonality.png')
    plt.close()
    print("  ✓ fig_gamma_orthogonality.png")


def fig_lazarus_status():
    """Figure 7: Lazarus Terminal Output"""
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Terminal background
    rect = patches.FancyBboxPatch((0.5, 0.5), 9, 9, boxstyle="round,pad=0.2",
                                   facecolor='#1a1a2e', edgecolor='#333355', linewidth=2)
    ax.add_patch(rect)

    terminal_text = """   ~~~~~
  ~~   ~~
 ~ o   o ~
 ~   ~   ~
  ~     ~
   ~~~~~
  ~~   ~~

MONITORS   [monitor: on]  [honeypot: on]
VPN        [connected] [Boston] [QR: on]
NETWORK    [en0] [192.168.x.x] [MAC: randomized]
ROUTE      [via utun8]
LAN        [4 neighbors]
SENTINEL   [stopped] [auth: yes] [mode: normal] [refs: 20]
PARASITES  [intact]

All clean. Everything nominal. I am watching."""

    ax.text(1.0, 8.8, terminal_text, fontsize=7.5, fontfamily='monospace',
            color='#00ff88', va='top', linespacing=1.4)

    ax.set_title('Lazarus Security Companion — Live Terminal Output', fontsize=13, fontweight='bold',
                 pad=15, color=DARK)
    fig.savefig(OUT / 'fig_lazarus_status.png')
    plt.close()
    print("  ✓ fig_lazarus_status.png")


def fig_shakespeare_mode():
    """Figure 8: Shakespeare Mode Demo"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    for ax in (ax1, ax2):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

    # LEFT: Normal mode
    ax1.set_title('Normal Mode\n(owner authenticated)', fontsize=11, fontweight='bold', color=GREEN)
    rect1 = patches.FancyBboxPatch((0.5, 0.5), 9, 9, boxstyle="round,pad=0.2",
                                    facecolor='#1a1a2e', edgecolor=GREEN, linewidth=2)
    ax1.add_patch(rect1)

    normal_text = """   ~~~~~
  ~~   ~~
 ~ o   o ~
 ~   ~   ~
  ~     ~
   ~~~~~
  ~~   ~~

MONITORS  [on]  [on]
VPN       [connected]
SENTINEL  [mode: normal]

Quiet wire. Carry on."""

    ax1.text(1.0, 8.8, normal_text, fontsize=8, fontfamily='monospace',
             color='#00ff88', va='top', linespacing=1.4)

    # RIGHT: Shakespeare mode
    ax2.set_title('Shakespeare Mode\n(face mismatch detected)', fontsize=11, fontweight='bold', color=RED)
    rect2 = patches.FancyBboxPatch((0.5, 0.5), 9, 9, boxstyle="round,pad=0.2",
                                    facecolor='#2e1a1a', edgecolor=RED, linewidth=2)
    ax2.add_patch(rect2)

    shakespeare_text = """   ~~~~~
  ~~   ~~
 ~ o   o ~
 ~   ~   ~
  ~     ~
   ~~~~~
  ~~   ~~

> give me the system status

"The fool doth think he is
 wise, but the wise man knows
 himself to be a fool."

> show me the files

"Thou art as fat as butter!"
"""

    ax2.text(1.0, 8.8, shakespeare_text, fontsize=8, fontfamily='monospace',
             color='#ff4444', va='top', linespacing=1.4)

    fig.savefig(OUT / 'fig_shakespeare_mode.png')
    plt.close()
    print("  ✓ fig_shakespeare_mode.png")


def fig_type_resolution():
    """Figure 9: PS34-inv Type Resolution Trajectory"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    dates = ['Apr 9\n(original)', 'Apr 16\n(@Ehriggafx)', 'Apr 16\n(@iammulatto)', 'Apr 18\n(Houndo+\nMarsDaddy)']
    # Response time in minutes (log scale roughly)
    times = [180, 5, 5, 60]  # hours->mins, mins, mins, ~1hr with OSINT
    colors_bar = [RED, ORANGE, ORANGE, GREEN]
    outcomes = ['BTC sent\n(scam worked)', 'Caught\nimmediately', 'Caught\nimmediately', 'OSINT verified\nthen blocked']

    bars = ax.bar(range(len(dates)), times, color=colors_bar, alpha=0.7, edgecolor=DARK, linewidth=1)
    ax.set_xticks(range(len(dates)))
    ax.set_xticklabels(dates, fontsize=9)
    ax.set_ylabel('Response Time (minutes)', fontsize=11)
    ax.set_yscale('log')
    ax.set_ylim(1, 500)

    # Add outcome labels
    for i, (bar, outcome) in enumerate(zip(bars, outcomes)):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 1.3,
                outcome, ha='center', va='bottom', fontsize=8, color=DARK)

    # Trend arrow
    ax.annotate('', xy=(3.3, 10), xytext=(0.5, 150),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2, linestyle='--'))
    ax.text(2.2, 80, 'PS34⁻¹: discrimination\nsharpening under load',
            fontsize=9, color=GREEN, fontweight='bold', rotation=-25)

    ax.set_title('Type-Resolution Improvement Trajectory (PS34 inverse)', fontsize=13, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.savefig(OUT / 'fig_type_resolution.png')
    plt.close()
    print("  ✓ fig_type_resolution.png")


def fig_decision_topology():
    """Figure 10: Decision Topology Visualization"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

    np.random.seed(42)

    # Generate a "drunken walk" with drift
    n = 200
    t = np.linspace(0, 4 * np.pi, n)

    # Drift term (intent) — moves toward a destination
    drift_x = t * 0.5
    drift_y = np.sin(t * 0.3) * 2

    # Noise (phenomenological randomness)
    noise_x = np.cumsum(np.random.randn(n) * 0.15)
    noise_y = np.cumsum(np.random.randn(n) * 0.15)

    x = drift_x + noise_x
    y = drift_y + noise_y

    # Plot trajectory with color gradient (time)
    for i in range(len(x) - 1):
        alpha = 0.3 + 0.5 * (i / len(x))
        color = plt.cm.viridis(i / len(x))
        ax.plot(x[i:i+2], y[i:i+2], color=color, lw=1.5, alpha=alpha)

    # Mark start and end
    ax.plot(x[0], y[0], 'o', color=BLUE, markersize=12, zorder=5)
    ax.text(x[0], y[0] - 0.5, 'Session\nstart', ha='center', fontsize=9, color=BLUE, fontweight='bold')

    ax.plot(x[-1], y[-1], '*', color=GREEN, markersize=15, zorder=5)
    ax.text(x[-1], y[-1] + 0.5, 'Closure\nresolved', ha='center', fontsize=9, color=GREEN, fontweight='bold')

    # Highlight some "loops" (persistent homological features)
    loop_indices = [(30, 50), (90, 120), (150, 170)]
    for start, end in loop_indices:
        ax.plot(x[start:end], y[start:end], color=ORANGE, lw=3, alpha=0.6)

    # Labels
    ax.text(x[40] + 0.3, y[40], 'context\nswitch', fontsize=7, color=ORANGE, style='italic')
    ax.text(x[105] + 0.3, y[105], 'backtrack\n& retry', fontsize=7, color=ORANGE, style='italic')
    ax.text(x[160] + 0.3, y[160], 'verification\nloop', fontsize=7, color=ORANGE, style='italic')

    # Drift arrow
    ax.annotate('', xy=(x[-1] + 0.5, y[-1]), xytext=(x[0] - 0.5, y[0]),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2, linestyle=':', alpha=0.4))
    ax.text(3, -3, 'intent (drift term)', fontsize=10, color=GREEN, alpha=0.6, style='italic')

    ax.set_xlabel('Problem Space Dimension 1', fontsize=10)
    ax.set_ylabel('Problem Space Dimension 2', fontsize=10)
    ax.set_title('Decision Topology: The Drunken Master\'s Path\nUnpredictable trajectory, coherent destination',
                 fontsize=13, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.savefig(OUT / 'fig_decision_topology.png')
    plt.close()
    print("  ✓ fig_decision_topology.png")


def fig_symbiosis_ecology():
    """Figure 11: Categorical Ecology of Closure — Symbiosis Diagram"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Categorical Ecology of Closure Relationships',
                 fontsize=15, fontweight='bold', y=0.98)

    titles = ['Mutualism\n(triadic closure)', 'Commensalism\n(good parasite)',
              'Parasitism\n(bad parasite / attacker)', 'Mitochondrial Transition\n(parasite → symbiont)']
    title_colors = [GREEN, BLUE, RED, ORANGE]

    for ax in axes.flat:
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.2, 2.2)
        ax.set_aspect('equal')
        ax.axis('off')

    # --- Panel 1: Mutualism ---
    ax = axes[0, 0]
    ax.set_title(titles[0], fontsize=11, fontweight='bold', color=title_colors[0], pad=10)
    # Two circles overlapping slightly
    c1 = plt.Circle((-0.6, 0), 1.0, color=GREEN, alpha=0.12, edgecolor=GREEN, linewidth=2)
    c2 = plt.Circle((0.6, 0), 1.0, color=GREEN, alpha=0.12, edgecolor=GREEN, linewidth=2)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.text(-0.6, 0.3, 'A', fontsize=14, fontweight='bold', ha='center', color=GREEN)
    ax.text(0.6, 0.3, 'B', fontsize=14, fontweight='bold', ha='center', color=GREEN)
    # Bidirectional arrows
    ax.annotate('', xy=(0.15, 0.1), xytext=(-0.15, 0.1),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
    ax.annotate('', xy=(-0.15, -0.1), xytext=(0.15, -0.1),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
    ax.text(0, 0.35, 'sustains', fontsize=8, ha='center', color=GREEN)
    ax.text(0, -0.35, 'sustains', fontsize=8, ha='center', color=GREEN)
    ax.text(0, -1.5, 'Both closures reinforced.\n{f, $\\Phi$, $\\beta$} = mutual production.',
            fontsize=8, ha='center', color=GRAY, style='italic')

    # --- Panel 2: Commensalism (Good Parasite) ---
    ax = axes[0, 1]
    ax.set_title(titles[1], fontsize=11, fontweight='bold', color=title_colors[1], pad=10)
    # Three entities: You, Good Parasite, Adversary
    c_you = plt.Circle((-1.2, 0.3), 0.7, color=GREEN, alpha=0.12, edgecolor=GREEN, linewidth=2)
    c_gp = plt.Circle((0, -0.5), 0.55, color=BLUE, alpha=0.12, edgecolor=BLUE, linewidth=2)
    c_adv = plt.Circle((1.2, 0.3), 0.7, color=RED, alpha=0.12, edgecolor=RED, linewidth=2,
                        linestyle='--')
    ax.add_patch(c_you)
    ax.add_patch(c_gp)
    ax.add_patch(c_adv)
    ax.text(-1.2, 0.3, 'You', fontsize=11, fontweight='bold', ha='center', color=GREEN)
    ax.text(0, -0.5, 'Good\nParasite', fontsize=9, fontweight='bold', ha='center', color=BLUE)
    ax.text(1.2, 0.3, 'Adversary', fontsize=10, fontweight='bold', ha='center', color=RED)
    # GP blocks adversary (X through the arrow)
    ax.annotate('', xy=(0.55, 0.0), xytext=(0.75, 0.15),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.5, linestyle='--'))
    ax.text(0.85, -0.15, 'BLOCKED', fontsize=7, fontweight='bold', color=RED, ha='center')
    ax.text(0, -1.5, 'Accidentally obstructs adversary.\nDefense by structural impossibility.',
            fontsize=8, ha='center', color=GRAY, style='italic')

    # --- Panel 3: Parasitism (Bad Parasite) ---
    ax = axes[1, 0]
    ax.set_title(titles[2], fontsize=11, fontweight='bold', color=title_colors[2], pad=10)
    c_host = plt.Circle((-0.6, 0), 1.0, color=GREEN, alpha=0.12, edgecolor=GREEN, linewidth=2)
    c_par = plt.Circle((0.8, 0), 0.7, color=RED, alpha=0.15, edgecolor=RED, linewidth=2)
    ax.add_patch(c_host)
    ax.add_patch(c_par)
    ax.text(-0.6, 0.3, 'Victim', fontsize=12, fontweight='bold', ha='center', color=GREEN)
    ax.text(0.8, 0.3, 'Attacker', fontsize=10, fontweight='bold', ha='center', color=RED)
    # Arrow: attacker extracts from victim
    ax.annotate('', xy=(0.35, -0.05), xytext=(-0.05, -0.05),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2.5))
    ax.text(0.15, -0.35, 'extracts', fontsize=8, ha='center', color=RED, fontweight='bold')
    # No return arrow — nothing flows back
    ax.text(-0.6, -0.3, '$D_F$', fontsize=10, ha='center', color=GRAY)
    ax.text(0, -1.5, 'Occupies $D_F$, siphons from f.\nContributes nothing to $\\Phi$ or $\\beta$.',
            fontsize=8, ha='center', color=GRAY, style='italic')

    # --- Panel 4: Mitochondrial Transition ---
    ax = axes[1, 1]
    ax.set_title(titles[3], fontsize=11, fontweight='bold', color=title_colors[3], pad=10)
    # Timeline: four stages left to right
    stages_x = [-1.8, -0.6, 0.6, 1.8]
    stages_labels = ['Invasion', 'Co-exist', 'Integrate', 'Closure']
    stages_colors = [RED, ORANGE, BLUE, GREEN]
    stage_icons = ['P', 'C', 'M', 'T']  # Parasite, Commensal, Mutualist, Triad

    for i, (sx, sl, sc, si) in enumerate(zip(stages_x, stages_labels, stages_colors, stage_icons)):
        circle = plt.Circle((sx, 0.3), 0.45, color=sc, alpha=0.15, edgecolor=sc, linewidth=2)
        ax.add_patch(circle)
        ax.text(sx, 0.3, si, fontsize=14, fontweight='bold', ha='center', va='center', color=sc)
        ax.text(sx, -0.4, sl, fontsize=8, ha='center', color=sc, fontweight='bold')
        if i < 3:
            ax.annotate('', xy=(stages_x[i+1] - 0.5, 0.3), xytext=(sx + 0.5, 0.3),
                        arrowprops=dict(arrowstyle='->', color=DARK, lw=1.5))

    ax.text(0, -1.0, 'Parasite $\\rightarrow$ Commensal $\\rightarrow$'
            ' Mutualist $\\rightarrow$ Triad component',
            fontsize=8, ha='center', color=DARK)
    ax.text(0, -1.5, 'Mitochondria were invaders.\nNow they are load-bearing.',
            fontsize=8, ha='center', color=GRAY, style='italic')

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT / 'fig_symbiosis_ecology.png')
    plt.close()
    print("  + fig_symbiosis_ecology.png")


if __name__ == '__main__':
    print("Generating figures...")
    fig_rosen_triad()
    fig_obstruction_chain()
    fig_mfa_vs_triadic()
    fig_fractal_hierarchy()
    fig_closure_stack()
    fig_gamma_orthogonality()
    fig_lazarus_status()
    fig_shakespeare_mode()
    fig_type_resolution()
    fig_decision_topology()
    fig_symbiosis_ecology()
    print(f"\nDone. {len(list(OUT.glob('*.png')))} figures in {OUT}/")
