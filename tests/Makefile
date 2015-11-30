RUN=sudo python
SCRIPT=run_test.py
ARGS=1 1 1000
TESTS=reinvite-uac reinvite-uas reinvite-3pcc reinvite-proactive-3pcc reinvite-proactive-extension-3pcc refer-3pcc join-3pcc

.PHONY: $(TESTS) all clean

ORDER=order

REINVITE-UAC-DIR=reinvite-uac
REINVITE-UAC-DIR-TITLE="reINVITE scenario - UAC trigger"

REINVITE-UAS-DIR=reinvite-uas
REINVITE-UAS-DIR-TITLE="reINVITE scenario - UAS trigger"

REINVITE-3PCC-DIR=reinvite-3pcc
REINVITE-3PCC-TITLE="3pcc reINVITE scenario"

REINVITE-PROACTIVE-3PCC-DIR=reinvite-proactive-3pcc
REINVITE-PROACTIVE-3PCC-TITLE="3pcc proactive reINVITE scenario"

REINVITE-PROACTIVE-EXTENSION-3PCC-DIR=reinvite-proactive-extension-3pcc
REINVITE-PROACTIVE-EXTENSION-3PCC-TITLE="3pcc proactive reINVITE with extension scenario"

REFER-3PCC-DIR=refer-3pcc
REFER-3PCC-TITLE="3pcc REFER scenario"

JOIN-3PCC-DIR=join-3pcc
JOIN-3PCC-TITLE="3pcc JOIN scenario"

all: $(TESTS)

reinvite-uac:
	$(RUN) $(SCRIPT) $(REINVITE-UAC-DIR) $(REINVITE-UAC-DIR-TITLE) $(ARGS)

reinvite-uas:
	$(RUN) $(SCRIPT) $(REINVITE-UAS-DIR) $(REINVITE-UAS-DIR-TITLE) $(ARGS)

reinvite-3pcc:
	$(RUN) $(SCRIPT) $(REINVITE-3PCC-DIR) $(REINVITE-3PCC-TITLE) $(ARGS)

reinvite-proactive-3pcc:
	$(RUN) $(SCRIPT) $(REINVITE-PROACTIVE-3PCC-DIR) $(REINVITE-PROACTIVE-3PCC-TITLE) $(ARGS)

reinvite-proactive-extension-3pcc:
	$(RUN) $(SCRIPT) $(REINVITE-PROACTIVE-EXTENSION-3PCC-DIR) $(REINVITE-PROACTIVE-EXTENSION-3PCC-TITLE) $(ARGS)

refer-3pcc:
	$(RUN) $(SCRIPT) $(REFER-3PCC-DIR) $(REFER-3PCC-TITLE) $(ARGS)

join-3pcc:
	$(RUN) $(SCRIPT) $(JOIN-3PCC-DIR) $(JOIN-3PCC-TITLE) $(ARGS)

clean:
	-@cd $(REINVITE-UAC-DIR); echo "cleaning" `pwd`; rm -rf *.pcap *.png *.out $(ORDER); cd ..
	
	-@cd $(REINVITE-UAS-DIR); echo "cleaning" `pwd`; rm -rf *.pcap *.png *.out $(ORDER); cd ..
	
	-@cd $(REINVITE-3PCC-DIR); echo "cleaning" `pwd`; rm -rf *.pcap *.png *.out $(ORDER); cd ..
	
	-@cd $(REINVITE-PROACTIVE-3PCC-DIR); echo "cleaning" `pwd`; rm -rf *.pcap *.png *.out $(ORDER); cd ..
	
	-@cd $(REINVITE-PROACTIVE-EXTENSION-3PCC-DIR); echo "cleaning" `pwd`; rm -rf *.pcap *.png *.out $(ORDER); cd ..
	
	-@cd $(REFER-3PCC-DIR); echo "cleaning" `pwd`; rm -rf *.pcap *.png *.out $(ORDER); cd ..
	
	-@cd $(JOIN-3PCC-DIR); echo "cleaning" `pwd`; rm -rf *.pcap *.png *.out $(ORDER); cd ..
