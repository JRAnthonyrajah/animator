"""
Main entry point for animator.
"""

import logging
from my_project import hello

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Main application entry point."""
    logger.info("Starting animator...")
    print(hello())
    logger.info("Application completed successfully")


if __name__ == "__main__":
    main()
