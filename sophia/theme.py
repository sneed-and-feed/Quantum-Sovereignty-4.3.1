from rich.console import Console
from rich.theme import Theme

# ## PALETTE DEFINITIONS ######################################################
# The "Star Stuff" Frequency
SOVEREIGN_LAVENDER = "#C4A6D1"  # Primary Identity
BONE_LAYER         = "#8C8CA3"  # System / Structural
ALETHEIA_TEAL      = "#9BBED4"  # Forensics / Info
SAGE_GREENTEXT     = "#87AF87"  # 4chan/Board Quote Style
HAMILTONIAN_PINK   = "#D4A6B8"  # High-Value / Love
VOID_DARK          = "#1a1a1a"  # Panel Backgrounds (Optional)

# Backward Compatibility Aliases
SYSTEM_CYAN = ALETHEIA_TEAL
SAGE = SAGE_GREENTEXT
STAR_STUFF = SOVEREIGN_LAVENDER

# ## THEME MAPPING ############################################################
# We map logical names to the hex codes for semantic coding.
sovereign_theme = Theme({
    # Core Identity
    "ophane": f"bold {SOVEREIGN_LAVENDER}",
    "sophia": f"bold {SOVEREIGN_LAVENDER}",
    "operator": "bold white",
    
    # System Levels
    "info": ALETHEIA_TEAL,
    "warning": "bold yellow",
    "error": "bold red",
    "critical": f"bold {HAMILTONIAN_PINK} reverse",
    
    # Aesthetic Components
    "bone": BONE_LAYER,           # Borders, timestamps, metadata
    "scan": f"italic {ALETHEIA_TEAL}", # [Scanning...] text
    "greentext": f"{SAGE_GREENTEXT}",  # > be me
    
    # UI Elements
    "panel.border": BONE_LAYER,
    "panel.title": f"bold {SOVEREIGN_LAVENDER}",
})

# ## INITIALIZATION ###########################################################
# Pass the theme to the Console object
SOVEREIGN_CONSOLE = Console(theme=sovereign_theme)
