VERSION=5.1.1
RELEASE=casa-release-${VERSION}-5.el7

all: pack


${RELEASE}:
	wget https://casa.nrao.edu/download/distro/linux/release/el7/${RELEASE}.tar.gz

${RELEASE}/: ${RELEASE}
	tar zxvf ${RELEASE}.tar.gz

casalite-${VERSION}/: ${RELEASE}
	cp ${RELEASE}/ casalite-${VERSION}/

pack: casalite-${VERSION}/
	echo "yes"
