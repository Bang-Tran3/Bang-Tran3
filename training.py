from logging_config import get_logger

logger = get_logger(__name__)

def start_training():
    logger.info("Training started")
    try:
        reward = 0.75
        logger.info(f"Current reward: {reward}")
    except Exception as e:
        # Just log it—AWS is watching for the "ERROR" keyword!
        logger.error(f"ERROR: Training failed - {str(e)}")
