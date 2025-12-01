# Type Checking Imports
# ---------------------
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Any

# Standard Library Imports
# ------------------------

# Third Party Imports
# -------------------
from qtpy import QtCore, QtGui, QtWidgets

# Local Imports
# -------------


# Constant Definitions
# --------------------


# Class Definitions
# -----------------
class MyWidget(QtWidgets.QWidget):
    """Template QWidget with stubbed setup hooks.

    Attributes:
        ...
    """

    # Initialization and Setup
    # ------------------------
    def __init__(self, parent: QtWidgets.QWidget = None):
        """Set up the widget, build the UI, and connect signals.

        Args:
            parent: Optional parent widget.
        """
        super().__init__(parent)

        # Store the arguments
        ...

        # Initialize setup
        self.__init_attributes()
        self.__init_ui()
        self.__init_signal_connections()

    def __init_attributes(self):
        """Initialize attributes.
        """
        ...

    def __init_ui(self):
        """Initialize the UI.
        """
        # Initial UI State
        # ----------------
        ...

        # Create Widgets
        # --------------
        ...

        # Add Widgets to Layouts
        # ----------------------
        ...

    def __init_signal_connections(self):
        """Initialize signal-slot connections.
        """
        ...

    # Public Methods
    # --------------

    # Class Properties
    # ----------------

    # Utility Methods
    # ---------------

    # Private Methods
    # ---------------

    # Special Methods
    # ---------------

    # Overridden Methods
    # ------------------


# Main Function
# -------------
def main():
    """Create the application, and show the widget.
    """
    import sys

    # Argument Parsing
    # ----------------
    ...

    # Application Setup and Execution
    # -------------------------------
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
