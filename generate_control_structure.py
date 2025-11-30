"""
Control Structure Diagram Generator for 7125CEM Assignment
Generates a professional hierarchical control structure diagram for Level 4 Autonomous Vehicle
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set up the figure with high DPI for professional quality
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Define colors for different levels
colors = {
    'governance': '#E8F4F8',      # Light blue
    'management': '#FFF4E6',       # Light orange
    'actuators': '#E8F5E9',        # Light green
    'process': '#F3E5F5',          # Light purple
    'control': '#FFE0B2',          # Amber for control actions
    'feedback': '#C8E6C9',         # Green for feedback
    'border': '#263238'            # Dark grey for borders
}

def draw_box(ax, x, y, width, height, text, color, fontsize=9, bold=False):
    """Draw a box with text"""
    box = FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.05",
        edgecolor=colors['border'],
        facecolor=color,
        linewidth=2
    )
    ax.add_patch(box)

    weight = 'bold' if bold else 'normal'
    ax.text(
        x + width/2, y + height/2, text,
        ha='center', va='center',
        fontsize=fontsize,
        weight=weight,
        wrap=True
    )

def draw_arrow(ax, x1, y1, x2, y2, label='', style='solid', color='black', width=1.5):
    """Draw an arrow between two points"""
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='->,head_width=0.3,head_length=0.3',
        linestyle=style,
        linewidth=width,
        color=color,
        mutation_scale=20
    )
    ax.add_patch(arrow)

    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x + 0.2, mid_y, label, fontsize=7,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='none', alpha=0.8))

# ============================================================================
# LEVEL 1: GOVERNANCE LAYER (Top)
# ============================================================================
level1_y = 10.5
ax.text(8, 11.5, 'LEVEL 1: GOVERNANCE', ha='center', fontsize=12, weight='bold')

draw_box(ax, 0.5, level1_y, 4.5, 0.8, 'Regulatory Authorities\n(Safety Standards)', colors['governance'], fontsize=8)
draw_box(ax, 5.5, level1_y, 4.5, 0.8, 'Manufacturers\n(Design Requirements)', colors['governance'], fontsize=8)
draw_box(ax, 10.5, level1_y, 5, 0.8, 'Infrastructure Providers\n(V2I Communication)', colors['governance'], fontsize=8)

# ============================================================================
# LEVEL 2: SYSTEM MANAGEMENT (Controllers)
# ============================================================================
level2_y = 7.5
ax.text(8, 9.2, 'LEVEL 2: SYSTEM MANAGEMENT (Primary Controllers)', ha='center', fontsize=12, weight='bold')

# Route Planning Module
draw_box(ax, 0.5, level2_y, 3.5, 1.2,
         'Route Planning\nModule\n\n• Generates routes\n• Calculates waypoints\n• Journey estimates',
         colors['management'], fontsize=7.5)

# Autonomous Driving AI System (Main Controller)
draw_box(ax, 4.5, level2_y, 3.5, 1.2,
         'Autonomous Driving\nAI System\n\n• Decision making\n• Control commands\n• Safety logic',
         colors['management'], fontsize=7.5, bold=True)

# Sensor Fusion Module
draw_box(ax, 8.5, level2_y, 3.5, 1.2,
         'Sensor Fusion\nModule\n\n• Environmental model\n• Multi-modal data\n• Object detection',
         colors['management'], fontsize=7.5)

# HMI Controller
draw_box(ax, 12.5, level2_y, 3, 1.2,
         'HMI Controller\n\n• Passenger info\n• Override interface\n• Alerts',
         colors['management'], fontsize=7.5)

# ============================================================================
# LEVEL 3: ACTUATORS & SENSORS
# ============================================================================
level3_y_actuators = 5.5
level3_y_sensors = 4.5

ax.text(8, 6.5, 'LEVEL 3: ACTUATORS & SENSORS', ha='center', fontsize=12, weight='bold')

# Actuators
draw_box(ax, 0.5, level3_y_actuators, 2.3, 0.7, 'Steering\nActuator', colors['actuators'], fontsize=7)
draw_box(ax, 3.0, level3_y_actuators, 2.3, 0.7, 'Brake\nActuator', colors['actuators'], fontsize=7)
draw_box(ax, 5.5, level3_y_actuators, 2.3, 0.7, 'Throttle\nActuator', colors['actuators'], fontsize=7)

# Sensors (staggered below actuators)
draw_box(ax, 8.2, level3_y_sensors, 1.8, 0.6, 'Cameras\n(8x 360°)', colors['actuators'], fontsize=6.5)
draw_box(ax, 10.2, level3_y_sensors, 1.8, 0.6, 'LIDAR\n(4x 200m)', colors['actuators'], fontsize=6.5)
draw_box(ax, 12.2, level3_y_sensors, 1.8, 0.6, 'Radar\n(6x 300m)', colors['actuators'], fontsize=6.5)
draw_box(ax, 14.2, level3_y_sensors, 1.5, 0.6, 'GPS/IMU', colors['actuators'], fontsize=6.5)

draw_box(ax, 8.2, level3_y_sensors - 0.8, 1.8, 0.6, 'Ultrasonic\n(12x)', colors['actuators'], fontsize=6.5)
draw_box(ax, 10.2, level3_y_sensors - 0.8, 1.8, 0.6, 'Weather\nSensors', colors['actuators'], fontsize=6.5)

# ============================================================================
# LEVEL 4: CONTROLLED PROCESS
# ============================================================================
level4_y = 1.5
ax.text(8, 2.8, 'LEVEL 4: CONTROLLED PROCESS (Environment)', ha='center', fontsize=12, weight='bold')

draw_box(ax, 0.5, level4_y, 15, 1,
         'Vehicle Dynamics | Road Conditions | Traffic | Weather | Pedestrians | Cyclists | Other Vehicles',
         colors['process'], fontsize=8)

# ============================================================================
# CONTROL LOOPS & ARROWS
# ============================================================================

# Governance to Management (downward commands)
draw_arrow(ax, 2.75, level1_y, 2.25, level2_y + 1.2, 'Safety\nStandards', color='#1976D2')
draw_arrow(ax, 7.75, level1_y, 6.25, level2_y + 1.2, 'Design\nReqs', color='#1976D2')
draw_arrow(ax, 13, level1_y, 11, level2_y + 1.2, 'V2I\nData', color='#1976D2')

# Route Planning to AI
draw_arrow(ax, 4, level2_y + 0.5, 4.5, level2_y + 0.5, 'Route\nData', color='#F57C00', width=2)

# Sensor Fusion to AI
draw_arrow(ax, 8.5, level2_y + 0.5, 8, level2_y + 0.5, 'Environment\nModel', color='#F57C00', width=2)

# HMI to AI
draw_arrow(ax, 12.5, level2_y + 0.5, 8, level2_y + 0.8, 'Passenger\nCommands', color='#F57C00', style='dashed')

# AI to Actuators (Control Actions)
draw_arrow(ax, 5.5, level2_y, 1.6, level3_y_actuators + 0.7, 'Steer\nCommand', color='#D32F2F', width=2)
draw_arrow(ax, 6, level2_y, 4.15, level3_y_actuators + 0.7, 'Brake\nCommand', color='#D32F2F', width=2)
draw_arrow(ax, 6.5, level2_y, 6.65, level3_y_actuators + 0.7, 'Throttle\nCommand', color='#D32F2F', width=2)

# Actuators to Controlled Process
draw_arrow(ax, 1.6, level3_y_actuators, 2, level4_y + 1, color='#388E3C', width=2)
draw_arrow(ax, 4.15, level3_y_actuators, 5, level4_y + 1, color='#388E3C', width=2)
draw_arrow(ax, 6.65, level3_y_actuators, 7.5, level4_y + 1, color='#388E3C', width=2)

# Sensors reading from Controlled Process (Feedback)
draw_arrow(ax, 9, level4_y + 1, 9.1, level3_y_sensors + 0.6, style='dashed', color='#7B1FA2', width=1.5)
draw_arrow(ax, 11, level4_y + 1, 11.1, level3_y_sensors + 0.6, style='dashed', color='#7B1FA2', width=1.5)
draw_arrow(ax, 13, level4_y + 1, 13.1, level3_y_sensors + 0.6, style='dashed', color='#7B1FA2', width=1.5)
draw_arrow(ax, 14.5, level4_y + 1, 14.9, level3_y_sensors + 0.6, style='dashed', color='#7B1FA2', width=1.5)

# Sensors to Sensor Fusion
draw_arrow(ax, 9.1, level3_y_sensors, 9.5, level2_y, 'Sensor\nData', color='#7B1FA2', style='dashed', width=1.5)
draw_arrow(ax, 11.1, level3_y_sensors, 10.5, level2_y, '', color='#7B1FA2', style='dashed', width=1.5)
draw_arrow(ax, 13.1, level3_y_sensors, 11, level2_y, '', color='#7B1FA2', style='dashed', width=1.5)

# GPS feedback to Route Planning
draw_arrow(ax, 14.9, level3_y_sensors, 3.5, level2_y, 'Position\nFeedback', color='#7B1FA2', style='dashed', width=1.5)

# ============================================================================
# LEGEND
# ============================================================================
legend_y = 0.3
legend_elements = [
    mpatches.Patch(color='#1976D2', label='Governance Commands'),
    mpatches.Patch(color='#D32F2F', label='Control Actions'),
    mpatches.Patch(color='#388E3C', label='Physical Actuation'),
    mpatches.Patch(color='#7B1FA2', label='Feedback/Sensor Data'),
    mpatches.Patch(color='#F57C00', label='Inter-Controller Communication')
]

ax.legend(handles=legend_elements, loc='lower center', ncol=5,
          bbox_to_anchor=(0.5, -0.05), fontsize=8, frameon=True)

# Title
plt.suptitle('Level 4 Autonomous Vehicle - Hierarchical Control Structure\nSTPA Analysis - 7125CEM Assignment',
             fontsize=14, weight='bold', y=0.98)

# Add subtitle with key control loops
ax.text(8, 0.1,
        'Key Control Loops: ① Speed Control ② Lateral Control ③ Obstacle Avoidance ④ Route Adaptation ⑤ Passenger Interaction ⑥ Sensor Health ⑦ Weather Adaptation ⑧ V2I Communication',
        ha='center', fontsize=7, style='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()

# Save the figure
plt.savefig('Control_Structure_Diagram.png', dpi=300, bbox_inches='tight')
plt.savefig('Control_Structure_Diagram.pdf', dpi=300, bbox_inches='tight')
print("[OK] Control Structure Diagram saved as PNG and PDF")
plt.close()
