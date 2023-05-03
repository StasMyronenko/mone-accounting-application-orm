from typing import Callable

from config.db import Session


def handle_session_error(func: Callable, do_commit=True, **kwargs):
    res = None
    with Session() as session:
        try:
            res = func(session, **kwargs)
        except Exception as e:
            session.rollback()
            raise e
        else:
            if do_commit:
                session.commit()
    return res
