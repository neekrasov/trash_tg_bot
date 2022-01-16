import logging
from aiogram.utils.exceptions import (TelegramAPIError, MessageNotModified, CantParseEntities, Unauthorized,
                                      InvalidQueryID, CantDemoteChatCreator, MessageToDeleteNotFound,
                                      MessageTextIsEmpty, RetryAfter, MessageCantBeDeleted, BadRequest
                                      )

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, MessageNotModified):
        logging.exception(f'Message is not modified: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, Unauthorized):
        logging.exception(f'Unauthorized: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, InvalidQueryID):
        logging.exception(f"Invalid query id: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, CantDemoteChatCreator):
        logging.exception(f"Can't remote chat creator: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.exception(f'Message to delete not found: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.exception(f'Message text is empty: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, RetryAfter):
        logging.exception(f'Retry after: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.exception(f"Message can't be deleted: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, BadRequest):
        logging.exception(f'Bad request: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    logging.exception(f'Update: {update} \n{exception}')
