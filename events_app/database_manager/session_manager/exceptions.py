class MissingSessionError(Exception):
    """
    Exception raised for when the user tries to access a database_manager session before it is created.
    """

    def __init__(self):
        msg = """
        No session found! Either you are not currently in a request context,
        or you need to manually create a session context by using a `db` instance as
        a context manager e.g.:

        async with db():
            await db.session.execute(foo.select()).fetchall()
        """

        super().__init__(msg)


class SessionNotInitialisedError(Exception):
    """
    Exception raised when the user creates a new DB session without first initialising it.
    """

    def __init__(self):
        msg = """
        Session not initialised! Ensure that DBSessionMiddleware has been initialised before
        attempting database_manager access.
        """

        super().__init__(msg)
