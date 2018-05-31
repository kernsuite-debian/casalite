VERSION=5.1.2
RELEASE=casa-release-${VERSION}-4.el7

all: pack

${RELEASE}.tar.gz:
	wget https://casa.nrao.edu/download/distro/linux/release/el7/${RELEASE}.tar.gz

${RELEASE}/: ${RELEASE}.tar.gz
	echo "extracting ${RELEASE}.tar.gz"
	tar zxf ${RELEASE}.tar.gz

casalite-${VERSION}/: ${RELEASE}/
	cp -a ${RELEASE}/ casalite-${VERSION}/
	rm -rf casalite-${VERSION}/Pipeline-CASA51*
	rm -rf casalite-${VERSION}/pipeline
	rm -rf casalite-${VERSION}/etc/carta
	rm -rf casalite-${VERSION}/data/demo

casalite-${VERSION}.tar.xz: casalite-${VERSION}/
	tar Jcvf casalite-${VERSION}.tar.xz casalite-${VERSION}/

pack: casalite-${VERSION}.tar.xz
	echo "done"
