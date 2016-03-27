# Functions used by other files, but not used directly in parent code


class MiscError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def jsonify_receps(recep_input, recep_type, silent):

    json_return = ''
    if not silent:
        if recep_type == "cc":
            json_return = '"CcRecipients":['
        elif recep_type == "to":
            json_return = '"ToRecipients":['
        elif recep_type == "bcc":
            json_return = '"BccRecipients":['
        else:
            raise MiscError('To or CC recipients not provided')

    receps = recep_input.split(',')
    for num in range(len(receps)):
        receps[num] = receps[num].strip()

    for m in range(0, len(receps)):
        if len(receps) - m == 1:
            insert = receps[m].replace('"', "'")
            json_return += '{ "EmailAddress": { "Address": "' + insert + '" } }'
        else:
            insert = receps[m].replace('"', "'")
            json_return += '{ "EmailAddress": { "Address": "' + insert + '" } },'

    return json_return