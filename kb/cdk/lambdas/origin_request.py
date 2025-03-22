import logging

logger = logging.getLogger("OriginRequest")
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(event)
    origin_request = event["Records"][0]["cf"]["request"]
    if origin_request["uri"].endswith("/"):
        origin_request["uri"] = origin_request["uri"] + "index.html"
    logger.info(origin_request)
    return origin_request
