Name:           ros-kinetic-ar-track-alvar
Version:        0.6.2
Release:        0%{?dist}
Summary:        ROS ar_track_alvar package

Group:          Development/Libraries
License:        LGPL-2.1
URL:            http://ros.org/wiki/ar_track_alvar
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-ar-track-alvar-msgs
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-pcl-conversions
Requires:       ros-kinetic-pcl-ros
Requires:       ros-kinetic-resource-retriever
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf2
Requires:       ros-kinetic-visualization-msgs
Requires:       tinyxml-devel
BuildRequires:  ros-kinetic-ar-track-alvar-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-pcl-conversions
BuildRequires:  ros-kinetic-pcl-ros
BuildRequires:  ros-kinetic-resource-retriever
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf2
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  tinyxml-devel

%description
This package is a ROS wrapper for Alvar, an open source AR tag tracking library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Feb 07 2017 Scott Niekum <sniekum@cs.umass.edu> - 0.6.2-0
- Autogenerated by Bloom

* Wed Jun 08 2016 Scott Niekum <sniekum@cs.umass.edu> - 0.6.1-0
- Autogenerated by Bloom

* Wed Jun 01 2016 Scott Niekum <sniekum@cs.umass.edu> - 0.6.0-0
- Autogenerated by Bloom

