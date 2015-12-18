subarch: amd64
target: stage4
version_stamp: hardened+cloud-latest
rel_type: hardened
profile: hardened/linux/amd64
snapshot: latest
source_subpath: hardened/stage3-amd64-hardened-latest
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
portage_confdir: /home/release/releng/releases/weekly/portage/cloud-stages

stage4/use:
	bash-completion
	bzip2
	idm
	ipv6
	mmx
	sse
	sse2
	urandom

stage4/packages:
	app-admin/logrotate
	app-admin/sudo
	app-admin/syslog-ng
	app-editors/vim
	app-emulation/cloud-init
	app-portage/eix
	app-portage/gentoolkit
	net-misc/dhcpcd
	sys-boot/grub
	sys-apps/dmidecode
	sys-apps/gptfdisk
	sys-apps/iproute2
	sys-apps/lsb-release
	sys-apps/pciutils
	sys-block/parted
	sys-devel/bc
	sys-power/acpid
	sys-process/cronie
stage4/fsscript: /home/release/releng/releases/weekly/scripts/cloud-prep.sh
stage4/root_overlay: /home/release/releng/releases/weekly/overlays/cloud-overlay
stage4/rcadd:
	acpid|default
	cloud-config|default
	cloud-final|default
	cloud-init-local|default
	cloud-init|default
	cronie|default
	dhcpcd|default
	net.lo|default
	netmount|default
	sshd|default
	syslog-ng|default

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /home/release/releng/releases/weekly/kconfig/amd64/installcd-3.18.12.config
boot/kernel/gentoo/extraversion: openstack
boot/kernel/gentoo/gk_kernargs: --all-ramdisk-modules
