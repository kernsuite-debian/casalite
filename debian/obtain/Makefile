.PHONY: all pack

VERSION=5.6.0
RELEASE=casa-release-${VERSION}-60.el7

all: pack

${RELEASE}.tar.gz:
	wget https://casa.nrao.edu/download/distro/linux/release/el7/${RELEASE}.tar.gz

${RELEASE}/: ${RELEASE}.tar.gz
	tar zxmvf ${RELEASE}.tar.gz

casalite-${VERSION}/: ${RELEASE}/
	cp -a ${RELEASE}/ casalite-${VERSION}/
	rm -rf casalite-${VERSION}/Pipeline-CASA*
	rm -rf casalite-${VERSION}/pipeline
	rm -rf casalite-${VERSION}/etc/carta
	rm -rf casalite-${VERSION}/data/alma
	rm -rf casalite-${VERSION}/data/demo
	rm -rf casalite-${VERSION}/share/doc

casalite-${VERSION}.tar.xz: casalite-${VERSION}/
	tar Jcvf casalite-${VERSION}.tar.xz casalite-${VERSION}/

pack: casalite-${VERSION}.tar.xz
	echo "done"
