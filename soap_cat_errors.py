from cleaninty.nintendowifi.soapenvelopebase import SoapCodeError
# not too sure where to put this so...
# i realized cleaninty has error things built in so i'm just gonna take some of those and modify them a smidge


class NoDonors(Exception):
    def __init__(self, *args, **kwds):
        message = kwds.pop(
            "message", "Uh oh! someone forgot to fill in the message for NoDonors"
        )

        super().__init__(*args, **kwds)

        self._message = message

    @property
    def message(self) -> str:
        return self._message


class BorkedDonor(SoapCodeError):
    def __init__(self, *args, **kwds):
        donor_name = kwds.pop("donor_name", "why is donor_name empty")
        soapcodeerror: SoapCodeError = kwds.pop("soapcodeerror", None)

        super().__init__(*args, **kwds)

        self._donor_name = donor_name
        self._soapcodeerror = soapcodeerror

    @property
    def donor_name(self) -> str:
        return self._donor_name

    @property
    def soapcodeerror(self) -> SoapCodeError:
        return self._soapcodeerror
