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
    """A Qt widget that performs some task.

    Attributes:
        ...
    """

    # Initialization and Setup
    # ------------------------
    def __init__(self, parent: QtWidgets.QWidget = None):
        """Initialize the widget and set up the UI, signal connections, and icons.

        Args:
            ...
        """
        # Initialize the super class
        super().__init__(parent)

        # Store the arguments
        ...

        # Initialize setup
        self.__init_attributes()
        self.__init_ui()
        self.__init_signal_connections()

    def __init_attributes(self):
        """Initialize the attributes.
        """
        # Attributes
        # ----------
        ...

        # Private Attributes
        # ------------------
        ...

    def __init_ui(self):
        """Initialize the UI of the widget.
        """
        # Create Widgets
        # --------------
        ...

        # Add Widgets to Layouts
        # ----------------------
        ...

    def __init_signal_connections(self):
        """Initialize signal-slot connections.
        """
        # Connect signals to slots
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
    # Create the application and the main window
    app = QtWidgets.QApplication(sys.argv)

    # Create and show the widget
    widget = MyWidget()
    widget.show()

    # Run the application
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
