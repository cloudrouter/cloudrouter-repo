# Copyright 2015 CloudRouter Project Authors.

CR_VERSION	:= 2
CR_RELEASE	:= 1
REPO_BASE	:= https://raw.githubusercontent.com/cloudrouter/cloudrouter-release/$(CR_VERSION)-$(CR_RELEASE)/cloudrouter-release
REPOFILE	:= cloudrouter.repo
GPGKEY		:= RPM-GPG-KEY-cloudrouter-2-primary

all: source

$(REPOFILE):
	curl --output $(REPOFILE) $(REPO_BASE)/$(REPOFILE)
	sed -i -e 's/$$releasever/$(CR_VERSION)/' $(REPOFILE)
	grep "^gpgkey" $(REPOFILE) > /dev/null 2>&1 \
    	|| sed -i s+'^gpgcheck=1'+'gpgcheck=1\ngpgkey=file:///etc/pki/rpm-gpg/$(GPGKEY)'+ $(REPOFILE)

$(GPGKEY):
	curl --output $(GPGKEY) $(REPO_BASE)/$(GPGKEY)

source: $(REPOFILE) $(GPGKEY)

clean:
	rm -f $(REPOFILE) $(GPGKEY)
