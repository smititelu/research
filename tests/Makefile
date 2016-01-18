RUN=sudo python
ARGS=1 1 1000

SERVER-SCRIPT=run_test_server.py
SERVER-TESTS=server-reinvite-uac server-reinvite-uas server-options-uas server-reinvite-3pcc server-reinvite-proactive-3pcc server-reinvite-proactive-extension-3pcc server-refer-3pcc server-join-3pcc
SERVER-KAMAILIO-TESTS=server-kamailio-geolocation-1 server-kamailio-geolocation-2

CLIENT-SCRIPT=run_test_client.py
CLIENT-TESTS=client-reinvite-uac client-reinvite-uas client-options-uas client-reinvite-3pcc client-reinvite-proactive-3pcc client-reinvite-proactive-extension-3pcc client-refer-3pcc client-join-3pcc
CLIENT-KAMAILIO-TESTS=client-kamailio-geolocation-1 client-kamailio-geolocation-2

# Tests
REINVITE-UAC-TEST=reinvite-uac
REINVITE-UAC-TEST-TITLE="reINVITE scenario - UAC trigger"
REINVITE-UAC-TEST-FILES=$(filter-out $(wildcard $(REINVITE-UAC-TEST)\/xml), $(wildcard $(REINVITE-UAC-TEST)\/*))

REINVITE-UAS-TEST=reinvite-uas
REINVITE-UAS-TEST-TITLE="reINVITE scenario - UAS trigger"
REINVITE-UAS-TEST-FILES=$(filter-out $(wildcard $(REINVITE-UAS-TEST)\/xml), $(wildcard $(REINVITE-UAS-TEST)\/*))

OPTIONS-UAS-TEST=options-uas
OPTIONS-UAS-TEST-TITLE="OPTIONS geolocation scenario"
OPTIONS-UAS-TEST-FILES=$(filter-out $(wildcard $(OPTIONS-UAS-TEST)\/xml), $(wildcard $(OPTIONS-UAS-TEST)\/*))

REINVITE-3PCC-TEST=reinvite-3pcc
REINVITE-3PCC-TITLE="3pcc reINVITE scenario"
REINVITE-3PCC-TEST-FILES=$(filter-out $(wildcard $(REINVITE-3PCC-TEST)\/xml), $(wildcard $(REINVITE-3PCC-TEST)\/*))

REINVITE-PROACTIVE-3PCC-TEST=reinvite-proactive-3pcc
REINVITE-PROACTIVE-3PCC-TITLE="3pcc proactive reINVITE scenario"
REINVITE-PROACTIVE-3PCC-TEST-FILES=$(filter-out $(wildcard $(REINVITE-PROACTIVE-3PCC-TEST)\/xml), $(wildcard $(REINVITE-PROACTIVE-3PCC-TEST)\/*))

REINVITE-PROACTIVE-EXTENSION-3PCC-TEST=reinvite-proactive-extension-3pcc
REINVITE-PROACTIVE-EXTENSION-3PCC-TITLE="3pcc proactive reINVITE with extension scenario"
REINVITE-PROACTIVE-EXTENSION-3PCC-TEST-FILES=$(filter-out $(wildcard $(REINVITE-PROACTIVE-EXTENSION-3PCC-TEST)\/xml), $(wildcard $(REINVITE-PROACTIVE-EXTENSION-3PCC-TEST)\/*))

REFER-3PCC-TEST=refer-3pcc
REFER-3PCC-TITLE="3pcc REFER scenario"
REFER-3PCC-TEST-FILES=$(filter-out $(wildcard $(REFER-3PCC-TEST)\/xml), $(wildcard $(REFER-3PCC-TEST)\/*))

JOIN-3PCC-TEST=join-3pcc
JOIN-3PCC-TITLE="3pcc JOIN scenario"
JOIN-3PCC-TEST-FILES=$(filter-out $(wildcard $(JOIN-3PCC-TEST)\/xml), $(wildcard $(JOIN-3PCC-TEST)\/*))

KAMAILIO-GEOLOCATION-1-TEST=kamailio-geolocation-1
KAMAILIO-GEOLOCATION-1-TITLE="Kamailio Geolocation - one interface UAC"
KAMAILIO-GEOLOCATION-1-TEST-FILES=$(filter-out $(wildcard $(KAMAILIO-GEOLOCATION-1-TEST)\/xml), $(wildcard $(KAMAILIO-GEOLOCATION-1-TEST)\/*))

KAMAILIO-GEOLOCATION-2-TEST=kamailio-geolocation-2
KAMAILIO-GEOLOCATION-2-TITLE="Kamailio Geolocation - two interfaces UAC"
KAMAILIO-GEOLOCATION-2-TEST-FILES=$(filter-out $(wildcard $(KAMAILIO-GEOLOCATION-2-TEST)\/xml), $(wildcard $(KAMAILIO-GEOLOCATION-2-TEST)\/*))


.PHONY: $(CLIENT-TESTS) $(SERVER-TESTS) all clean


# client machine
client-all: $(CLIENT-TESTS)
client-kamailio-all: $(CLIENT-KAMAILIO-TESTS)

client-reinvite-uac:
	$(RUN) $(CLIENT-SCRIPT) $(REINVITE-UAC-TEST) $(REINVITE-UAC-TEST-TITLE) $(ARGS)

client-reinvite-uas:
	$(RUN) $(CLIENT-SCRIPT) $(REINVITE-UAS-TEST) $(REINVITE-UAS-TEST-TITLE) $(ARGS)

client-options-uas:
	$(RUN) $(CLIENT-SCRIPT) $(OPTIONS-UAS-TEST) $(OPTIONS-UAS-TEST-TITLE) $(ARGS)

client-reinvite-3pcc:
	$(RUN) $(CLIENT-SCRIPT) $(REINVITE-3PCC-TEST) $(REINVITE-3PCC-TITLE) $(ARGS)

client-reinvite-proactive-3pcc:
	$(RUN) $(CLIENT-SCRIPT) $(REINVITE-PROACTIVE-3PCC-TEST) $(REINVITE-PROACTIVE-3PCC-TITLE) $(ARGS)

client-reinvite-proactive-extension-3pcc:
	$(RUN) $(CLIENT-SCRIPT) $(REINVITE-PROACTIVE-EXTENSION-3PCC-TEST) $(REINVITE-PROACTIVE-EXTENSION-3PCC-TITLE) $(ARGS)

client-refer-3pcc:
	$(RUN) $(CLIENT-SCRIPT) $(REFER-3PCC-TEST) $(REFER-3PCC-TITLE) $(ARGS)

client-join-3pcc:
	$(RUN) $(CLIENT-SCRIPT) $(JOIN-3PCC-TEST) $(JOIN-3PCC-TITLE) $(ARGS)

client-kamailio-geolocation-1:
	$(RUN) $(CLIENT-SCRIPT) $(KAMAILIO-GEOLOCATION-1-TEST) $(KAMAILIO-GEOLOCATION-1-TITLE) $(ARGS)

client-kamailio-geolocation-2:
	$(RUN) $(CLIENT-SCRIPT) $(KAMAILIO-GEOLOCATION-2-TEST) $(KAMAILIO-GEOLOCATION-2-TITLE) $(ARGS)


# server machine
server-all: $(SERVER-TESTS)
server-kamailio-all: $(SERVER-KAMAILIO-TESTS)

server-reinvite-uac:
	$(RUN) $(SERVER-SCRIPT) $(REINVITE-UAC-TEST) $(REINVITE-UAC-TEST-TITLE) $(ARGS)

server-reinvite-uas:
	$(RUN) $(SERVER-SCRIPT) $(REINVITE-UAS-TEST) $(REINVITE-UAS-TEST-TITLE) $(ARGS)

server-options-uas:
	$(RUN) $(SERVER-SCRIPT) $(OPTIONS-UAS-TEST) $(OPTIONS-UAS-TEST-TITLE) $(ARGS)

server-reinvite-3pcc:
	$(RUN) $(SERVER-SCRIPT) $(REINVITE-3PCC-TEST) $(REINVITE-3PCC-TITLE) $(ARGS)

server-reinvite-proactive-3pcc:
	$(RUN) $(SERVER-SCRIPT) $(REINVITE-PROACTIVE-3PCC-TEST) $(REINVITE-PROACTIVE-3PCC-TITLE) $(ARGS)

server-reinvite-proactive-extension-3pcc:
	$(RUN) $(SERVER-SCRIPT) $(REINVITE-PROACTIVE-EXTENSION-3PCC-TEST) $(REINVITE-PROACTIVE-EXTENSION-3PCC-TITLE) $(ARGS)

server-refer-3pcc:
	$(RUN) $(SERVER-SCRIPT) $(REFER-3PCC-TEST) $(REFER-3PCC-TITLE) $(ARGS)

server-join-3pcc:
	$(RUN) $(SERVER-SCRIPT) $(JOIN-3PCC-TEST) $(JOIN-3PCC-TITLE) $(ARGS)

server-kamailio-geolocation-1:
	$(RUN) $(SERVER-SCRIPT) $(KAMAILIO-GEOLOCATION-1-TEST) $(KAMAILIO-GEOLOCATION-1-TITLE) $(ARGS)

server-kamailio-geolocation-2:
	$(RUN) $(SERVER-SCRIPT) $(KAMAILIO-GEOLOCATION-2-TEST) $(KAMAILIO-GEOLOCATION-2-TITLE) $(ARGS)


# clean
clean:
	-@echo "cleaning" $(REINVITE-UAC-TEST)/; rm -rf $(REINVITE-UAC-TEST-FILES)
	-@echo "cleaning" $(REINVITE-UAS-TEST)/; rm -rf $(REINVITE-UAS-TEST-FILES)
	-@echo "cleaning" $(OPTIONS-UAS-TEST)/; rm -rf $(OPTIONS-UAS-TEST-FILES)
	-@echo "cleaning" $(REINVITE-3PCC-TEST)/; rm -rf $(REINVITE-3PCC-TEST-FILES)
	-@echo "cleaning" $(REINVITE-PROACTIVE-3PCC-TEST)/; rm -rf $(REINVITE-PROACTIVE-3PCC-TEST-FILES)
	-@echo "cleaning" $(REINVITE-PROACTIVE-EXTENSION-3PCC-TEST)/; rm -rf $(REINVITE-PROACTIVE-EXTENSION-3PCC-TEST-FILES)
	-@echo "cleaning" $(REFER-3PCC-TEST)/; rm -rf $(REFER-3PCC-TEST-FILES)
	-@echo "cleaning" $(JOIN-3PCC-TEST)/; rm -rf $(JOIN-3PCC-TEST-FILES)
	-@echo "cleaning" $(KAMAILIO-GEOLOCATION-1-TEST)/; rm -rf $(KAMAILIO-GEOLOCATION-1-TEST-FILES)
	-@echo "cleaning" $(KAMAILIO-GEOLOCATION-2-TEST)/; rm -rf $(KAMAILIO-GEOLOCATION-2-TEST-FILES)
