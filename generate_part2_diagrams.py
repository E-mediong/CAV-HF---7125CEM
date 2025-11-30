"""
Part 2 Human Error Analysis Visualizations for 7125CEM Assignment
Generates diagrams for the Phoenix Stratocruiser scenario analysis
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
import numpy as np

# ============================================================================
# FIGURE 1: Endsley's Situation Awareness Model Applied to Scenario
# ============================================================================

fig1, ax1 = plt.subplots(1, 1, figsize=(14, 10))
ax1.set_xlim(0, 14)
ax1.set_ylim(0, 10)
ax1.axis('off')

def draw_box_fig1(x, y, width, height, text, color, fontsize=9):
    box = FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.1",
        edgecolor='black',
        facecolor=color,
        linewidth=2
    )
    ax1.add_patch(box)
    ax1.text(x + width/2, y + height/2, text, ha='center', va='center',
             fontsize=fontsize, wrap=True)

def draw_arrow_fig1(x1, y1, x2, y2, label='', color='black', style='solid'):
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='->,head_width=0.4,head_length=0.4',
        linestyle=style,
        linewidth=2,
        color=color,
        mutation_scale=20
    )
    ax1.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax1.text(mid_x + 0.3, mid_y, label, fontsize=8,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='black'))

# Title
ax1.text(7, 9.5, "Endsley's Situation Awareness Model\nApplied to Phoenix Stratocruiser Navigation Error",
         ha='center', fontsize=13, weight='bold')

# Level 1 SA: Perception
draw_box_fig1(1, 7, 3.5, 1.2,
             'LEVEL 1 SA:\nPERCEPTION\n\nElements perceived\nin environment',
             '#FFE0B2', fontsize=9)

ax1.text(2.75, 6.5, 'FAILURES:', ha='center', fontsize=8, weight='bold', color='red')
ax1.text(2.75, 6.1, '• "Half an eye on traffic"\n• Dark, rainy conditions\n• Small, unclear map\n• Looking at meeting notes\n• Making phone calls\n• Passive passenger role',
         ha='center', fontsize=7, va='top',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFCDD2'))

# Level 2 SA: Comprehension
draw_box_fig1(5.25, 7, 3.5, 1.2,
             'LEVEL 2 SA:\nCOMPREHENSION\n\nUnderstanding of\ncurrent situation',
             '#C5E1A5', fontsize=9)

ax1.text(7, 6.5, 'FAILURES:', ha='center', fontsize=8, weight='bold', color='red')
ax1.text(7, 6.1, '• Diversions seem plausible\n• Both routes via Cambridge\n• "The car has it all under control"\n• Wrong schema activated\n• Expectation bias',
         ha='center', fontsize=7, va='top',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFCDD2'))

# Level 3 SA: Projection
draw_box_fig1(9.5, 7, 3.5, 1.2,
             'LEVEL 3 SA:\nPROJECTION\n\nFuture state\nprediction',
             '#B3E5FC', fontsize=9)

ax1.text(11.25, 6.5, 'FAILURES:', ha='center', fontsize=8, weight='bold', color='red')
ax1.text(11.25, 6.1, '• No arrival time projection\n• "Got there very quickly"\n• No mental model of journey\n• Didn\'t notice time passing',
         ha='center', fontsize=7, va='top',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFCDD2'))

# Arrows showing progression
draw_arrow_fig1(4.5, 7.6, 5.25, 7.6, '', color='#1976D2', style='solid')
draw_arrow_fig1(8.75, 7.6, 9.5, 7.6, '', color='#1976D2', style='solid')

# Bottom layer: Contributing Factors
draw_box_fig1(1, 3.5, 12, 1.8,
             'CONTRIBUTING FACTORS TO SA DEGRADATION\n\n' +
             'Automation-Induced Complacency • Vigilance Decrement • Out-of-the-Loop Performance Problem\n' +
             'Cognitive Tunneling (meeting prep) • High Workload • Fatigue • Time Pressure\n' +
             'Automation Bias • Mode Confusion • Inadequate HMI Feedback • Environmental Masking',
             '#F3E5F5', fontsize=8)

# Arrows from factors to SA levels
draw_arrow_fig1(4, 3.5, 2.75, 7, '', color='red', style='dashed')
draw_arrow_fig1(7, 3.5, 7, 7, '', color='red', style='dashed')
draw_arrow_fig1(10, 3.5, 11.25, 7, '', color='red', style='dashed')

# Outcome
draw_box_fig1(3, 1, 8, 1.2,
             'OUTCOME:\n90-Mile Navigation Error Undetected Until Arrival\n"You don\'t recognise anything" - Complete SA Breakdown',
             '#FFCDD2', fontsize=9)

draw_arrow_fig1(7, 3.5, 7, 2.2, '', color='red', style='solid')

# Reference
ax1.text(7, 0.3, 'Based on: Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems.\nHuman Factors, 37(1), 32-64.',
         ha='center', fontsize=7, style='italic')

plt.tight_layout()
plt.savefig('Part2_Endsley_SA_Model.png', dpi=300, bbox_inches='tight')
plt.savefig('Part2_Endsley_SA_Model.pdf', dpi=300, bbox_inches='tight')
print("[OK] Endsley SA Model diagram saved as PNG and PDF")

# ============================================================================
# FIGURE 2: Reason's Swiss Cheese Model for Navigation Error
# ============================================================================

fig2, ax2 = plt.subplots(1, 1, figsize=(14, 8))
ax2.set_xlim(0, 14)
ax2.set_ylim(0, 8)
ax2.axis('off')

# Title
ax2.text(7, 7.5, "Reason's Swiss Cheese Model - Navigation Error Propagation",
         ha='center', fontsize=13, weight='bold')

ax2.text(7, 7, 'Multiple defensive layers with aligned "holes" allowed error to propagate to completion',
         ha='center', fontsize=9, style='italic')

# Define layers (cheese slices)
layers = [
    {'x': 1.5, 'name': 'HMI Design', 'color': '#FFE082'},
    {'x': 3.5, 'name': 'Initial\nVerification', 'color': '#FFCC80'},
    {'x': 5.5, 'name': 'En Route\nMonitoring', 'color': '#FFAB91'},
    {'x': 7.5, 'name': 'SA\nMaintenance', 'color': '#FF8A65'},
    {'x': 9.5, 'name': 'Anomaly\nDetection', 'color': '#EF5350'},
    {'x': 11.5, 'name': 'Environmental\nCues', 'color': '#E53935'}
]

# Draw each cheese slice with holes
np.random.seed(42)
for layer in layers:
    # Draw slice
    rect = FancyBboxPatch(
        (layer['x'] - 0.4, 1.5), 0.8, 4,
        boxstyle="round,pad=0.05",
        edgecolor='black',
        facecolor=layer['color'],
        linewidth=2,
        alpha=0.7
    )
    ax2.add_patch(rect)

    # Add label
    ax2.text(layer['x'], 6, layer['name'], ha='center', fontsize=8, weight='bold')

    # Add "holes" (failures) - create random holes but ensure they align
    hole_y = 3.5  # Aligned hole position
    circle = Circle((layer['x'], hole_y), 0.25, facecolor='white',
                   edgecolor='black', linewidth=1.5)
    ax2.add_patch(circle)

# Draw arrow showing error propagation through aligned holes
arrow_y = 3.5
ax2.annotate('', xy=(12.5, arrow_y), xytext=(0.5, arrow_y),
            arrowprops=dict(arrowstyle='->', lw=4, color='red'))

ax2.text(0.3, arrow_y, 'ERROR', fontsize=10, weight='bold', color='red',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='yellow'))

ax2.text(12.8, arrow_y, 'ACCIDENT', fontsize=10, weight='bold', color='red',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFCDD2'))

# Add specific failures for each layer
failures = [
    'No disambiguation\nSmall map\nNo confirmation',
    'Automation bias\nTime pressure\nFatigue',
    'Complacency\nOOTL problem\nPassive role',
    'Divided attention\nCognitive tunneling\nWorkload',
    'Diversions plausible\nExpectation bias\nNo alerts',
    'Dark/rainy\nUnfamiliar roads\nFew landmarks'
]

for i, (layer, failure) in enumerate(zip(layers, failures)):
    ax2.text(layer['x'], 1, failure, ha='center', fontsize=6.5,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9))

# Reference
ax2.text(7, 0.2, 'Based on: Reason, J. (2008). The human contribution: Unsafe acts, accidents and heroic recoveries. Ashgate.',
         ha='center', fontsize=7, style='italic')

plt.tight_layout()
plt.savefig('Part2_Swiss_Cheese_Model.png', dpi=300, bbox_inches='tight')
plt.savefig('Part2_Swiss_Cheese_Model.pdf', dpi=300, bbox_inches='tight')
print("[OK] Swiss Cheese Model diagram saved as PNG and PDF")

# ============================================================================
# FIGURE 3: Cognitive Biases & Error Cascade
# ============================================================================

fig3, ax3 = plt.subplots(1, 1, figsize=(12, 10))
ax3.set_xlim(0, 12)
ax3.set_ylim(0, 10)
ax3.axis('off')

# Title
ax3.text(6, 9.5, 'Cognitive Biases and Error Cascade\nPhoenix Stratocruiser Navigation Failure',
         ha='center', fontsize=13, weight='bold')

# Phase 1: Initial Error
ax3.text(6, 8.7, 'PHASE 1: INITIAL ERROR (Destination Selection)', ha='center',
        fontsize=10, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFE082'))

biases_initial = [
    {'name': 'Confirmation\nBias', 'desc': 'Saw "Broughton",\nassumed correct', 'x': 1.5, 'y': 7.5},
    {'name': 'Satisficing', 'desc': 'First match\n"good enough"', 'x': 4, 'y': 7.5},
    {'name': 'Availability\nHeuristic', 'desc': 'Parents\' location\ndominates', 'x': 6.5, 'y': 7.5},
    {'name': 'Recognition\nvs Recall', 'desc': 'Recognized name,\nno recall check', 'x': 9, 'y': 7.5},
]

for bias in biases_initial:
    box = FancyBboxPatch(
        (bias['x'] - 0.6, bias['y'] - 0.4), 1.2, 0.8,
        boxstyle="round,pad=0.05",
        edgecolor='black', facecolor='#FFCDD2', linewidth=1.5
    )
    ax3.add_patch(box)
    ax3.text(bias['x'], bias['y'] + 0.15, bias['name'], ha='center', fontsize=7, weight='bold')
    ax3.text(bias['x'], bias['y'] - 0.15, bias['desc'], ha='center', fontsize=6)

# Arrow to amplifiers
ax3.annotate('', xy=(6, 6.5), xytext=(6, 7.1),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))

# Contextual Amplifiers
ax3.text(6, 6.3, 'CONTEXTUAL AMPLIFIERS', ha='center', fontsize=9, weight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF9C4'))

amplifiers = ['High Cognitive Load', 'Time Pressure', 'Fatigue', 'New Vehicle\n(2 days)', 'Automation Trust']
for i, amp in enumerate(amplifiers):
    x_pos = 1.5 + i * 2.2
    ax3.text(x_pos, 5.8, amp, ha='center', fontsize=7,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFECB3'))

# Phase 2: Detection Failure
ax3.annotate('', xy=(6, 4.8), xytext=(6, 5.5),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))

ax3.text(6, 4.5, 'PHASE 2: DETECTION FAILURE (En Route)', ha='center',
        fontsize=10, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor='#FF8A65'))

detection_failures = [
    {'name': 'Automation\nBias', 'x': 2, 'y': 3.5},
    {'name': 'Mode\nConfusion', 'x': 4, 'y': 3.5},
    {'name': 'Complacency', 'x': 6, 'y': 3.5},
    {'name': 'OOTL\nProblem', 'x': 8, 'y': 3.5},
    {'name': 'Expectation\nBias', 'x': 10, 'y': 3.5},
]

for df in detection_failures:
    box = FancyBboxPatch(
        (df['x'] - 0.5, df['y'] - 0.3), 1, 0.6,
        boxstyle="round,pad=0.05",
        edgecolor='black', facecolor='#FFCDD2', linewidth=1.5
    )
    ax3.add_patch(box)
    ax3.text(df['x'], df['y'], df['name'], ha='center', fontsize=7, weight='bold')

# Contributing factors
ax3.annotate('', xy=(6, 2.3), xytext=(6, 3.2),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))

contrib_box = FancyBboxPatch(
    (0.5, 1.2), 11, 1,
    boxstyle="round,pad=0.1",
    edgecolor='black', facecolor='#E1F5FE', linewidth=2
)
ax3.add_patch(contrib_box)

ax3.text(6, 2, 'ADDITIONAL CONTRIBUTING FACTORS', ha='center', fontsize=8, weight='bold')
ax3.text(6, 1.7, 'Cognitive Tunneling (meeting prep) • Divided Attention (phone calls) • Vigilance Decrement\n' +
        'Poor HMI Feedback • Environmental Masking (dark, rainy) • Plausible Diversions (A47, A11 closed)',
        ha='center', fontsize=7)

# Final outcome
ax3.annotate('', xy=(6, 0.8), xytext=(6, 1.2),
            arrowprops=dict(arrowstyle='->', lw=3, color='red'))

outcome_box = FancyBboxPatch(
    (2, 0.1), 8, 0.6,
    boxstyle="round,pad=0.1",
    edgecolor='red', facecolor='#FFCDD2', linewidth=3
)
ax3.add_patch(outcome_box)

ax3.text(6, 0.4, 'OUTCOME: 90-mile error undetected until arrival\n"You don\'t recognise anything" - Buckinghamshire instead of Greater Manchester',
        ha='center', fontsize=8, weight='bold')

plt.tight_layout()
plt.savefig('Part2_Cognitive_Biases_Cascade.png', dpi=300, bbox_inches='tight')
plt.savefig('Part2_Cognitive_Biases_Cascade.pdf', dpi=300, bbox_inches='tight')
print("[OK] Cognitive Biases Cascade diagram saved as PNG and PDF")
plt.close('all')
