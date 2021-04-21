from burp import IBurpExtender
from burp import IBurpExtenderCallbacks
from burp import IHttpListener
from burp import IHttpRequestResponse
from burp import IRequestInfo
from burp import IExtensionHelpers
from burp import IParameter
from burp import IExtensionStateListener
from burp import ISessionHandlingAction
import sys
import json
import re
import uuid

class BurpExtender(IBurpExtender, IHttpListener):
	def registerExtenderCallbacks(self, callbacks):
		self._callbacks = callbacks
		self._callbacks.setExtensionName("UUID-Generator")
		self._callbacks.registerHttpListener(self)
		self._helpers = self._callbacks.getHelpers()
		sys.stdout = self._callbacks.getStdout()
		
		return
	def processHttpMessage(self,toolFlag, messageIsRequest, messageInfo):
		request = self._helpers.bytesToString(messageInfo.getRequest())
		request = request.replace("XXXX",str(uuid.uuid4()))
		messageInfo.setRequest(self._helpers.stringToBytes(request))
