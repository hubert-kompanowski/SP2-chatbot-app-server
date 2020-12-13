import json

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import AssistantV2


def test_response():
    test_data = ("9.1", "masks")

    config = json.load(open('chatbot_tests/wa_config.json'))

    authenticator = IAMAuthenticator(config['API_key'])

    assistant = AssistantV2(
        version='2020-04-01',
        authenticator=authenticator
    )
    assistant.set_service_url(config['URL'])
    response = assistant.message_stateless(
        assistant_id=config['assistant_id'],
        input={
            'message_type': 'text',
            'text': test_data[1]
        }
    ).get_result()

    assert (
        response['output']['intents'][0]['intent'].startswith(test_data[0])
    )
