action_list = [
    {
        "name" : "call.outbound_hangup", # should be the same as the type you send to the webhook
        "description" : "A call is hangup",
        "function_name": "create_call_outbound_hangup",
        "params": {}
    },
    {
        "name" : "call.inbound_start",
        "description" : "A call is started",
        "function_name": "create_call_inbound_start",
        "params": {}
    },
    {
        "name" : "call.outbound_start",
        "description" : "A call is started",
        "function_name": "create_call_outbound_start",
        "params": {}
    },
    {
        "name" : "media.recording.new",
        "description" : "A media is recorded",
        "function_name": "create_media_recording",
        "params": {}
    },
    {
        "name" : "call.inbound_hangup",
        "description" : "A call is hangup",
        "function_name": "create_call_inbound_hangup",
        "params": {}
    },
    {
        "name" : "billing.credit",
        "description" : "A billing credit",
        "function_name": "create_billing_credit",
        "params": {}
    },
    {
        "name" : "sms.mo",
        "description" : "A sms is sent",
        "function_name": "create_send_sms",
        "params": {}
    },
    {
        "name" : "did.assigned",
        "description" : "A did is assigned",
        "function_name": "create_did_assigned",
        "params": {}
    },
    {
        "name" : "did.unassigned",
        "description" : "A did is unassigned",
        "function_name": "create_did_unassigned",
        "params": {}
    }
]

reactions_list = [
    {
        "name": "makeCall",
		"description": "Make a call",
        "function_name": "make_call",
		"params": {"target": str, "msg": str}
    },
    {
        "name": "sendSms",
        "description": "Send a sms",
        "function_name": "send_sms",
        "params": {"target": str, "msg": str, "sender": str}
    },
    {
        "name": "createMedia",
		"description": "Create a media",
        "function_name": "create_media",
		"params": {"name": str}
    },
    {
        "name": "updateMediaTts",
		"description": "Update a media",
        "function_name": "update_media_tts",
		"params": {"id": str, "msg": str}
    },
    {
        "name": "getListOfMedias",
		"description": "Get list of medias",
        "function_name": "get_list_of_medias",
		"params": {"target": str}
    },
    {
        "name": "getQuotaStatus",
		"description": "Get quota status",
        "function_name": "get_quota_status",
        "params": {"target": str}
    }
]

