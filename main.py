# Authorization and misc functions
import retrieve
import create_message
import folders
from errors import MiscError, AuthError
import internal_methods


class OutlookAccount(object):
    """Summary of class here.

        Sets up access to Outlook account for all methods & classes.

        Attributes:
            access_token: A string OAuth token from Outlook allowing access to a user's account
        """

    def __init__(self, access_token):
        """Inits OutlookAccount with access_token."""
        if type(access_token) is None:
            raise AuthError('No access token provided with object instantiation.')
        self.access_token = access_token
        internal_methods.set_global_token__(access_token)

    def set_access_token(self, access_token):
        """
        Set the access token after creating an OutlookAccount object
        Args:
            access_token: A string representing the OAuth token
        """
        self.access_token = access_token
        internal_methods.set_global_token__(access_token)

    def __get_access_token(self):
        return self.access_token

    token = property(__get_access_token)

    # References
    ###
    # retrieve.py
    def get_message(self, message_id):
        """
        Retrieves the Outlook email matching the provided message_id
        Args:
            message_id: A string for the intended message, provided by Outlook

        Returns:
            A Message object
        """
        return retrieve.get_message(self, message_id)

    def get_messages(self):
        """Get first 10 messages in account, across all folders
        Returns:
            A list of Message objects.
        """
        return retrieve.get_messages(self, 0)

    def get_more_messages(self, page):
        """Retrieves additional messages, across all folders, indicated by 'page' number. get_messages() fetches page 1.
        Returns:
            List of Message objects
        """
        if not isinstance(page, int):
            print type(page)
            raise MiscError('page parameter must be of type integer')
        if page == 1:
            print 'Note that pulling the first page is equivalent to calling get_messages()'
        return retrieve.get_messages(self, page)

    def get_inbox(self):
        """
        Retrieves first ten messages in account's inbox
        Returns:
            List: of Message objects
        """
        return retrieve.get_inbox(self)

    # create_message.py
    @property
    def new_email(self):
        """Creates a NewMessage object
        Returns:
            object: NewMessage
        """
        return create_message.NewMessage(self.access_token)

    def get_sent_messages(self):
        """Retrieves last ten sent messages
        Returns:
            List[Message]
        """
        return retrieve.get_messages_from_folder_name(self, 'SentItems')

    def get_deleted_messages(self):
        """Retrieves last ten deleted messages
        Returns:
            List[Message]
        """
        return retrieve.get_messages_from_folder_name(self, 'DeletedItems')

    def get_draft_messages(self):
        """Retrieves last ten draft messages
        Returns:
            object:
        """
        return retrieve.get_messages_from_folder_name(self, 'Drafts')

    def get_folder_messages(self, folder):
        """Retrieve first ten messages from provided folder
        Args:
            folder: String providing the folder ID, from Outlook, to retrieve messages from

        Returns:
            List[Message]
        """
        return retrieve.get_messages_from_folder_name(self, folder)

    # folders
    def get_folders(self):
        """Retrieves a list of folders in the account
        Returns:
            List[Folder]
        """
        return folders.get_folders(self)

    def get_folder(self, folder_id):
        """Retrieve a Folder object matching the folder ID provided
        Args:
            folder_id: String identifying the Outlook folder to return
        Returns:
            object: Folder
        """
        return folders.get_folder(self, folder_id)

    def create_folder(self, parent_folder_id, new_folder_name):
        """
        Args:
            parent_folder_id: String identifying the folder that the new folder should be placed inside
            new_folder_name: String indicating the name the new folder should have
        Returns:
            object: Folder
        """
        return folders.create_folder(self, parent_folder_id, new_folder_name)
