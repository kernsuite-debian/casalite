VERSION=5.1.1
RELEASE=casa-release-${VERSION}-5.el7

all: pack

${RELEASE}.tar.gz:
	wget https://casa.nrao.edu/download/distro/linux/release/el7/${RELEASE}.tar.gz

${RELEASE}/: ${RELEASE}.tar.gz
	tar zxvf ${RELEASE}.tar.gz

casalite-${VERSION}/: ${RELEASE}/
	cp -a ${RELEASE}/ casalite-${VERSION}/
	rm -rf casalite-${VERSION}/Pipeline-CASA51-P2-B.40896
	rm -rf casalite-${VERSION}/pipeline
	rm -rf casalite-${VERSION}/etc/carta

casalite-${VERSION}.tar.xz: casalite-${VERSION}/
	tar Jcvf casalite-${VERSION}.tar.xz casalite-${VERSION}/

pack: casalite-${VERSION}.tar.xz
	echo "done"
