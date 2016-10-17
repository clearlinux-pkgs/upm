#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : upm
Version  : 0.8.0
Release  : 1
URL      : https://github.com/intel-iot-devkit/upm/archive/v0.8.0.tar.gz
Source0  : https://github.com/intel-iot-devkit/upm/archive/v0.8.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause BSD-3-Clause-Clear BSL-1.0 CC-BY-NC-SA-3.0 MIT
Requires: upm-lib
Requires: upm-python
BuildRequires : cmake
BuildRequires : libjpeg-turbo-dev
BuildRequires : mraa-dev
BuildRequires : nodejs
BuildRequires : nodejs-dev
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : swig

%description
UPM (Useful Packages & Modules) Sensor/Actuator repository for MRAA
==============

%package dev
Summary: dev components for the upm package.
Group: Development
Requires: upm-lib
Provides: upm-devel

%description dev
dev components for the upm package.


%package lib
Summary: lib components for the upm package.
Group: Libraries

%description lib
lib components for the upm package.


%package python
Summary: python components for the upm package.
Group: Default

%description python
python components for the upm package.


%prep
%setup -q -n upm-0.8.0

%build
export LANG=C
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd clr-build ; make test ; popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib/node_modules/jsupm_a110x/jsupm_a110x.node
/usr/lib/node_modules/jsupm_a110x/package.json
/usr/lib/node_modules/jsupm_ad8232/jsupm_ad8232.node
/usr/lib/node_modules/jsupm_ad8232/package.json
/usr/lib/node_modules/jsupm_adafruitms1438/jsupm_adafruitms1438.node
/usr/lib/node_modules/jsupm_adafruitms1438/package.json
/usr/lib/node_modules/jsupm_adafruitss/jsupm_adafruitss.node
/usr/lib/node_modules/jsupm_adafruitss/package.json
/usr/lib/node_modules/jsupm_adc121c021/jsupm_adc121c021.node
/usr/lib/node_modules/jsupm_adc121c021/package.json
/usr/lib/node_modules/jsupm_adis16448/jsupm_adis16448.node
/usr/lib/node_modules/jsupm_adis16448/package.json
/usr/lib/node_modules/jsupm_ads1x15/jsupm_ads1x15.node
/usr/lib/node_modules/jsupm_ads1x15/package.json
/usr/lib/node_modules/jsupm_adxl335/jsupm_adxl335.node
/usr/lib/node_modules/jsupm_adxl335/package.json
/usr/lib/node_modules/jsupm_adxl345/jsupm_adxl345.node
/usr/lib/node_modules/jsupm_adxl345/package.json
/usr/lib/node_modules/jsupm_adxrs610/jsupm_adxrs610.node
/usr/lib/node_modules/jsupm_adxrs610/package.json
/usr/lib/node_modules/jsupm_am2315/jsupm_am2315.node
/usr/lib/node_modules/jsupm_am2315/package.json
/usr/lib/node_modules/jsupm_apa102/jsupm_apa102.node
/usr/lib/node_modules/jsupm_apa102/package.json
/usr/lib/node_modules/jsupm_apds9002/jsupm_apds9002.node
/usr/lib/node_modules/jsupm_apds9002/package.json
/usr/lib/node_modules/jsupm_apds9930/jsupm_apds9930.node
/usr/lib/node_modules/jsupm_apds9930/package.json
/usr/lib/node_modules/jsupm_at42qt1070/jsupm_at42qt1070.node
/usr/lib/node_modules/jsupm_at42qt1070/package.json
/usr/lib/node_modules/jsupm_biss0001/jsupm_biss0001.node
/usr/lib/node_modules/jsupm_biss0001/package.json
/usr/lib/node_modules/jsupm_bma220/jsupm_bma220.node
/usr/lib/node_modules/jsupm_bma220/package.json
/usr/lib/node_modules/jsupm_bmi160/jsupm_bmi160.node
/usr/lib/node_modules/jsupm_bmi160/package.json
/usr/lib/node_modules/jsupm_bmp280/jsupm_bmp280.node
/usr/lib/node_modules/jsupm_bmp280/package.json
/usr/lib/node_modules/jsupm_bmpx8x/jsupm_bmpx8x.node
/usr/lib/node_modules/jsupm_bmpx8x/package.json
/usr/lib/node_modules/jsupm_bmx055/jsupm_bmx055.node
/usr/lib/node_modules/jsupm_bmx055/package.json
/usr/lib/node_modules/jsupm_bno055/jsupm_bno055.node
/usr/lib/node_modules/jsupm_bno055/package.json
/usr/lib/node_modules/jsupm_buzzer/jsupm_buzzer.node
/usr/lib/node_modules/jsupm_buzzer/package.json
/usr/lib/node_modules/jsupm_cjq4435/jsupm_cjq4435.node
/usr/lib/node_modules/jsupm_cjq4435/package.json
/usr/lib/node_modules/jsupm_cwlsxxa/jsupm_cwlsxxa.node
/usr/lib/node_modules/jsupm_cwlsxxa/package.json
/usr/lib/node_modules/jsupm_dfrph/jsupm_dfrph.node
/usr/lib/node_modules/jsupm_dfrph/package.json
/usr/lib/node_modules/jsupm_ds1307/jsupm_ds1307.node
/usr/lib/node_modules/jsupm_ds1307/package.json
/usr/lib/node_modules/jsupm_ds1808lc/jsupm_ds1808lc.node
/usr/lib/node_modules/jsupm_ds1808lc/package.json
/usr/lib/node_modules/jsupm_ds18b20/jsupm_ds18b20.node
/usr/lib/node_modules/jsupm_ds18b20/package.json
/usr/lib/node_modules/jsupm_ds2413/jsupm_ds2413.node
/usr/lib/node_modules/jsupm_ds2413/package.json
/usr/lib/node_modules/jsupm_ecs1030/jsupm_ecs1030.node
/usr/lib/node_modules/jsupm_ecs1030/package.json
/usr/lib/node_modules/jsupm_enc03r/jsupm_enc03r.node
/usr/lib/node_modules/jsupm_enc03r/package.json
/usr/lib/node_modules/jsupm_flex/jsupm_flex.node
/usr/lib/node_modules/jsupm_flex/package.json
/usr/lib/node_modules/jsupm_gas/jsupm_gas.node
/usr/lib/node_modules/jsupm_gas/package.json
/usr/lib/node_modules/jsupm_gp2y0a/jsupm_gp2y0a.node
/usr/lib/node_modules/jsupm_gp2y0a/package.json
/usr/lib/node_modules/jsupm_grove/jsupm_grove.node
/usr/lib/node_modules/jsupm_grove/package.json
/usr/lib/node_modules/jsupm_grovecollision/jsupm_grovecollision.node
/usr/lib/node_modules/jsupm_grovecollision/package.json
/usr/lib/node_modules/jsupm_groveehr/jsupm_groveehr.node
/usr/lib/node_modules/jsupm_groveehr/package.json
/usr/lib/node_modules/jsupm_groveeldriver/jsupm_groveeldriver.node
/usr/lib/node_modules/jsupm_groveeldriver/package.json
/usr/lib/node_modules/jsupm_groveelectromagnet/jsupm_groveelectromagnet.node
/usr/lib/node_modules/jsupm_groveelectromagnet/package.json
/usr/lib/node_modules/jsupm_groveemg/jsupm_groveemg.node
/usr/lib/node_modules/jsupm_groveemg/package.json
/usr/lib/node_modules/jsupm_grovegprs/jsupm_grovegprs.node
/usr/lib/node_modules/jsupm_grovegprs/package.json
/usr/lib/node_modules/jsupm_grovegsr/jsupm_grovegsr.node
/usr/lib/node_modules/jsupm_grovegsr/package.json
/usr/lib/node_modules/jsupm_grovelinefinder/jsupm_grovelinefinder.node
/usr/lib/node_modules/jsupm_grovelinefinder/package.json
/usr/lib/node_modules/jsupm_grovemd/jsupm_grovemd.node
/usr/lib/node_modules/jsupm_grovemd/package.json
/usr/lib/node_modules/jsupm_grovemoisture/jsupm_grovemoisture.node
/usr/lib/node_modules/jsupm_grovemoisture/package.json
/usr/lib/node_modules/jsupm_groveo2/jsupm_groveo2.node
/usr/lib/node_modules/jsupm_groveo2/package.json
/usr/lib/node_modules/jsupm_grovescam/jsupm_grovescam.node
/usr/lib/node_modules/jsupm_grovescam/package.json
/usr/lib/node_modules/jsupm_grovespeaker/jsupm_grovespeaker.node
/usr/lib/node_modules/jsupm_grovespeaker/package.json
/usr/lib/node_modules/jsupm_groveultrasonic/jsupm_groveultrasonic.node
/usr/lib/node_modules/jsupm_groveultrasonic/package.json
/usr/lib/node_modules/jsupm_grovevdiv/jsupm_grovevdiv.node
/usr/lib/node_modules/jsupm_grovevdiv/package.json
/usr/lib/node_modules/jsupm_grovewater/jsupm_grovewater.node
/usr/lib/node_modules/jsupm_grovewater/package.json
/usr/lib/node_modules/jsupm_grovewfs/jsupm_grovewfs.node
/usr/lib/node_modules/jsupm_grovewfs/package.json
/usr/lib/node_modules/jsupm_guvas12d/jsupm_guvas12d.node
/usr/lib/node_modules/jsupm_guvas12d/package.json
/usr/lib/node_modules/jsupm_h3lis331dl/jsupm_h3lis331dl.node
/usr/lib/node_modules/jsupm_h3lis331dl/package.json
/usr/lib/node_modules/jsupm_hcsr04/jsupm_hcsr04.node
/usr/lib/node_modules/jsupm_hcsr04/package.json
/usr/lib/node_modules/jsupm_hdxxvxta/jsupm_hdxxvxta.node
/usr/lib/node_modules/jsupm_hdxxvxta/package.json
/usr/lib/node_modules/jsupm_hlg150h/jsupm_hlg150h.node
/usr/lib/node_modules/jsupm_hlg150h/package.json
/usr/lib/node_modules/jsupm_hm11/jsupm_hm11.node
/usr/lib/node_modules/jsupm_hm11/package.json
/usr/lib/node_modules/jsupm_hmc5883l/jsupm_hmc5883l.node
/usr/lib/node_modules/jsupm_hmc5883l/package.json
/usr/lib/node_modules/jsupm_hmtrp/jsupm_hmtrp.node
/usr/lib/node_modules/jsupm_hmtrp/package.json
/usr/lib/node_modules/jsupm_hp20x/jsupm_hp20x.node
/usr/lib/node_modules/jsupm_hp20x/package.json
/usr/lib/node_modules/jsupm_ht9170/jsupm_ht9170.node
/usr/lib/node_modules/jsupm_ht9170/package.json
/usr/lib/node_modules/jsupm_htu21d/jsupm_htu21d.node
/usr/lib/node_modules/jsupm_htu21d/package.json
/usr/lib/node_modules/jsupm_hx711/jsupm_hx711.node
/usr/lib/node_modules/jsupm_hx711/package.json
/usr/lib/node_modules/jsupm_i2clcd/jsupm_i2clcd.node
/usr/lib/node_modules/jsupm_i2clcd/package.json
/usr/lib/node_modules/jsupm_ili9341/jsupm_ili9341.node
/usr/lib/node_modules/jsupm_ili9341/package.json
/usr/lib/node_modules/jsupm_ina132/jsupm_ina132.node
/usr/lib/node_modules/jsupm_ina132/package.json
/usr/lib/node_modules/jsupm_isd1820/jsupm_isd1820.node
/usr/lib/node_modules/jsupm_isd1820/package.json
/usr/lib/node_modules/jsupm_itg3200/jsupm_itg3200.node
/usr/lib/node_modules/jsupm_itg3200/package.json
/usr/lib/node_modules/jsupm_joystick12/jsupm_joystick12.node
/usr/lib/node_modules/jsupm_joystick12/package.json
/usr/lib/node_modules/jsupm_kxcjk1013/jsupm_kxcjk1013.node
/usr/lib/node_modules/jsupm_kxcjk1013/package.json
/usr/lib/node_modules/jsupm_l298/jsupm_l298.node
/usr/lib/node_modules/jsupm_l298/package.json
/usr/lib/node_modules/jsupm_l3gd20/jsupm_l3gd20.node
/usr/lib/node_modules/jsupm_l3gd20/package.json
/usr/lib/node_modules/jsupm_ldt0028/jsupm_ldt0028.node
/usr/lib/node_modules/jsupm_ldt0028/package.json
/usr/lib/node_modules/jsupm_lm35/jsupm_lm35.node
/usr/lib/node_modules/jsupm_lm35/package.json
/usr/lib/node_modules/jsupm_lol/jsupm_lol.node
/usr/lib/node_modules/jsupm_lol/package.json
/usr/lib/node_modules/jsupm_loudness/jsupm_loudness.node
/usr/lib/node_modules/jsupm_loudness/package.json
/usr/lib/node_modules/jsupm_lp8860/jsupm_lp8860.node
/usr/lib/node_modules/jsupm_lp8860/package.json
/usr/lib/node_modules/jsupm_lpd8806/jsupm_lpd8806.node
/usr/lib/node_modules/jsupm_lpd8806/package.json
/usr/lib/node_modules/jsupm_lsm303/jsupm_lsm303.node
/usr/lib/node_modules/jsupm_lsm303/package.json
/usr/lib/node_modules/jsupm_lsm9ds0/jsupm_lsm9ds0.node
/usr/lib/node_modules/jsupm_lsm9ds0/package.json
/usr/lib/node_modules/jsupm_m24lr64e/jsupm_m24lr64e.node
/usr/lib/node_modules/jsupm_m24lr64e/package.json
/usr/lib/node_modules/jsupm_max31723/jsupm_max31723.node
/usr/lib/node_modules/jsupm_max31723/package.json
/usr/lib/node_modules/jsupm_max31855/jsupm_max31855.node
/usr/lib/node_modules/jsupm_max31855/package.json
/usr/lib/node_modules/jsupm_max44000/jsupm_max44000.node
/usr/lib/node_modules/jsupm_max44000/package.json
/usr/lib/node_modules/jsupm_max44009/jsupm_max44009.node
/usr/lib/node_modules/jsupm_max44009/package.json
/usr/lib/node_modules/jsupm_max5487/jsupm_max5487.node
/usr/lib/node_modules/jsupm_max5487/package.json
/usr/lib/node_modules/jsupm_maxds3231m/jsupm_maxds3231m.node
/usr/lib/node_modules/jsupm_maxds3231m/package.json
/usr/lib/node_modules/jsupm_maxsonarez/jsupm_maxsonarez.node
/usr/lib/node_modules/jsupm_maxsonarez/package.json
/usr/lib/node_modules/jsupm_mcp9808/jsupm_mcp9808.node
/usr/lib/node_modules/jsupm_mcp9808/package.json
/usr/lib/node_modules/jsupm_mg811/jsupm_mg811.node
/usr/lib/node_modules/jsupm_mg811/package.json
/usr/lib/node_modules/jsupm_mhz16/jsupm_mhz16.node
/usr/lib/node_modules/jsupm_mhz16/package.json
/usr/lib/node_modules/jsupm_mic/jsupm_mic.node
/usr/lib/node_modules/jsupm_mic/package.json
/usr/lib/node_modules/jsupm_micsv89/jsupm_micsv89.node
/usr/lib/node_modules/jsupm_micsv89/package.json
/usr/lib/node_modules/jsupm_mlx90614/jsupm_mlx90614.node
/usr/lib/node_modules/jsupm_mlx90614/package.json
/usr/lib/node_modules/jsupm_mma7455/jsupm_mma7455.node
/usr/lib/node_modules/jsupm_mma7455/package.json
/usr/lib/node_modules/jsupm_mma7660/jsupm_mma7660.node
/usr/lib/node_modules/jsupm_mma7660/package.json
/usr/lib/node_modules/jsupm_mpl3115a2/jsupm_mpl3115a2.node
/usr/lib/node_modules/jsupm_mpl3115a2/package.json
/usr/lib/node_modules/jsupm_mpr121/jsupm_mpr121.node
/usr/lib/node_modules/jsupm_mpr121/package.json
/usr/lib/node_modules/jsupm_mpu9150/jsupm_mpu9150.node
/usr/lib/node_modules/jsupm_mpu9150/package.json
/usr/lib/node_modules/jsupm_mq303a/jsupm_mq303a.node
/usr/lib/node_modules/jsupm_mq303a/package.json
/usr/lib/node_modules/jsupm_ms5611/jsupm_ms5611.node
/usr/lib/node_modules/jsupm_ms5611/package.json
/usr/lib/node_modules/jsupm_my9221/jsupm_my9221.node
/usr/lib/node_modules/jsupm_my9221/package.json
/usr/lib/node_modules/jsupm_nlgpio16/jsupm_nlgpio16.node
/usr/lib/node_modules/jsupm_nlgpio16/package.json
/usr/lib/node_modules/jsupm_nrf24l01/jsupm_nrf24l01.node
/usr/lib/node_modules/jsupm_nrf24l01/package.json
/usr/lib/node_modules/jsupm_nrf8001/jsupm_nrf8001.node
/usr/lib/node_modules/jsupm_nrf8001/package.json
/usr/lib/node_modules/jsupm_nunchuck/jsupm_nunchuck.node
/usr/lib/node_modules/jsupm_nunchuck/package.json
/usr/lib/node_modules/jsupm_otp538u/jsupm_otp538u.node
/usr/lib/node_modules/jsupm_otp538u/package.json
/usr/lib/node_modules/jsupm_pca9685/jsupm_pca9685.node
/usr/lib/node_modules/jsupm_pca9685/package.json
/usr/lib/node_modules/jsupm_pn532/jsupm_pn532.node
/usr/lib/node_modules/jsupm_pn532/package.json
/usr/lib/node_modules/jsupm_ppd42ns/jsupm_ppd42ns.node
/usr/lib/node_modules/jsupm_ppd42ns/package.json
/usr/lib/node_modules/jsupm_pulsensor/jsupm_pulsensor.node
/usr/lib/node_modules/jsupm_pulsensor/package.json
/usr/lib/node_modules/jsupm_rfr359f/jsupm_rfr359f.node
/usr/lib/node_modules/jsupm_rfr359f/package.json
/usr/lib/node_modules/jsupm_rgbringcoder/jsupm_rgbringcoder.node
/usr/lib/node_modules/jsupm_rgbringcoder/package.json
/usr/lib/node_modules/jsupm_rhusb/jsupm_rhusb.node
/usr/lib/node_modules/jsupm_rhusb/package.json
/usr/lib/node_modules/jsupm_rotaryencoder/jsupm_rotaryencoder.node
/usr/lib/node_modules/jsupm_rotaryencoder/package.json
/usr/lib/node_modules/jsupm_rpr220/jsupm_rpr220.node
/usr/lib/node_modules/jsupm_rpr220/package.json
/usr/lib/node_modules/jsupm_servo/jsupm_servo.node
/usr/lib/node_modules/jsupm_servo/package.json
/usr/lib/node_modules/jsupm_si1132/jsupm_si1132.node
/usr/lib/node_modules/jsupm_si1132/package.json
/usr/lib/node_modules/jsupm_si114x/jsupm_si114x.node
/usr/lib/node_modules/jsupm_si114x/package.json
/usr/lib/node_modules/jsupm_si7005/jsupm_si7005.node
/usr/lib/node_modules/jsupm_si7005/package.json
/usr/lib/node_modules/jsupm_sm130/jsupm_sm130.node
/usr/lib/node_modules/jsupm_sm130/package.json
/usr/lib/node_modules/jsupm_smartdrive/jsupm_smartdrive.node
/usr/lib/node_modules/jsupm_smartdrive/package.json
/usr/lib/node_modules/jsupm_ssd1351/jsupm_ssd1351.node
/usr/lib/node_modules/jsupm_ssd1351/package.json
/usr/lib/node_modules/jsupm_st7735/jsupm_st7735.node
/usr/lib/node_modules/jsupm_st7735/package.json
/usr/lib/node_modules/jsupm_stepmotor/jsupm_stepmotor.node
/usr/lib/node_modules/jsupm_stepmotor/package.json
/usr/lib/node_modules/jsupm_sx1276/jsupm_sx1276.node
/usr/lib/node_modules/jsupm_sx1276/package.json
/usr/lib/node_modules/jsupm_sx6119/jsupm_sx6119.node
/usr/lib/node_modules/jsupm_sx6119/package.json
/usr/lib/node_modules/jsupm_t6713/jsupm_t6713.node
/usr/lib/node_modules/jsupm_t6713/package.json
/usr/lib/node_modules/jsupm_ta12200/jsupm_ta12200.node
/usr/lib/node_modules/jsupm_ta12200/package.json
/usr/lib/node_modules/jsupm_tcs3414cs/jsupm_tcs3414cs.node
/usr/lib/node_modules/jsupm_tcs3414cs/package.json
/usr/lib/node_modules/jsupm_teams/jsupm_teams.node
/usr/lib/node_modules/jsupm_teams/package.json
/usr/lib/node_modules/jsupm_tex00/jsupm_tex00.node
/usr/lib/node_modules/jsupm_tex00/package.json
/usr/lib/node_modules/jsupm_th02/jsupm_th02.node
/usr/lib/node_modules/jsupm_th02/package.json
/usr/lib/node_modules/jsupm_tm1637/jsupm_tm1637.node
/usr/lib/node_modules/jsupm_tm1637/package.json
/usr/lib/node_modules/jsupm_tsl2561/jsupm_tsl2561.node
/usr/lib/node_modules/jsupm_tsl2561/package.json
/usr/lib/node_modules/jsupm_ttp223/jsupm_ttp223.node
/usr/lib/node_modules/jsupm_ttp223/package.json
/usr/lib/node_modules/jsupm_ublox6/jsupm_ublox6.node
/usr/lib/node_modules/jsupm_ublox6/package.json
/usr/lib/node_modules/jsupm_uln200xa/jsupm_uln200xa.node
/usr/lib/node_modules/jsupm_uln200xa/package.json
/usr/lib/node_modules/jsupm_urm37/jsupm_urm37.node
/usr/lib/node_modules/jsupm_urm37/package.json
/usr/lib/node_modules/jsupm_vcap/jsupm_vcap.node
/usr/lib/node_modules/jsupm_vcap/package.json
/usr/lib/node_modules/jsupm_waterlevel/jsupm_waterlevel.node
/usr/lib/node_modules/jsupm_waterlevel/package.json
/usr/lib/node_modules/jsupm_wheelencoder/jsupm_wheelencoder.node
/usr/lib/node_modules/jsupm_wheelencoder/package.json
/usr/lib/node_modules/jsupm_wt5001/jsupm_wt5001.node
/usr/lib/node_modules/jsupm_wt5001/package.json
/usr/lib/node_modules/jsupm_xbee/jsupm_xbee.node
/usr/lib/node_modules/jsupm_xbee/package.json
/usr/lib/node_modules/jsupm_yg1006/jsupm_yg1006.node
/usr/lib/node_modules/jsupm_yg1006/package.json
/usr/lib/node_modules/jsupm_zfm20/jsupm_zfm20.node
/usr/lib/node_modules/jsupm_zfm20/package.json

%files dev
%defattr(-,root,root,-)
/usr/include/upm/a110x.hpp
/usr/include/upm/aci_queue.h
/usr/include/upm/aci_setup.h
/usr/include/upm/acilib.h
/usr/include/upm/ad8232.hpp
/usr/include/upm/adafruitms1438.hpp
/usr/include/upm/adafruitss.hpp
/usr/include/upm/adc121c021.hpp
/usr/include/upm/adis16448.hpp
/usr/include/upm/ads1015.hpp
/usr/include/upm/ads1115.hpp
/usr/include/upm/ads1x15.hpp
/usr/include/upm/adxl335.hpp
/usr/include/upm/adxl345.hpp
/usr/include/upm/adxrs610.hpp
/usr/include/upm/ak8975.hpp
/usr/include/upm/am2315.hpp
/usr/include/upm/apa102.hpp
/usr/include/upm/apds9002.hpp
/usr/include/upm/apds9930.hpp
/usr/include/upm/at42qt1070.hpp
/usr/include/upm/biss0001.hpp
/usr/include/upm/bma220.hpp
/usr/include/upm/bma250e.hpp
/usr/include/upm/bmc150.cxx
/usr/include/upm/bme280.hpp
/usr/include/upm/bmg160.hpp
/usr/include/upm/bmi055.hpp
/usr/include/upm/bmi160.hpp
/usr/include/upm/bmm150.hpp
/usr/include/upm/bmp280.hpp
/usr/include/upm/bmpx8x.hpp
/usr/include/upm/bmx055.hpp
/usr/include/upm/bno055.hpp
/usr/include/upm/buzzer.hpp
/usr/include/upm/cjq4435.hpp
/usr/include/upm/cwlsxxa.hpp
/usr/include/upm/dfrph.hpp
/usr/include/upm/ds1307.hpp
/usr/include/upm/ds1808lc.hpp
/usr/include/upm/ds18b20.hpp
/usr/include/upm/ds2413.hpp
/usr/include/upm/eboled.hpp
/usr/include/upm/ecs1030.hpp
/usr/include/upm/enc03r.hpp
/usr/include/upm/es08a.hpp
/usr/include/upm/es9257.hpp
/usr/include/upm/flex.hpp
/usr/include/upm/gas.hpp
/usr/include/upm/gp2y0a.hpp
/usr/include/upm/grove.hpp
/usr/include/upm/grovebase.hpp
/usr/include/upm/grovebutton.hpp
/usr/include/upm/grovecircularled.hpp
/usr/include/upm/grovecollision.hpp
/usr/include/upm/groveehr.hpp
/usr/include/upm/groveeldriver.hpp
/usr/include/upm/groveelectromagnet.hpp
/usr/include/upm/groveemg.hpp
/usr/include/upm/grovegprs.hpp
/usr/include/upm/grovegsr.hpp
/usr/include/upm/groveled.hpp
/usr/include/upm/groveledbar.hpp
/usr/include/upm/grovelight.hpp
/usr/include/upm/grovelinefinder.hpp
/usr/include/upm/grovemd.hpp
/usr/include/upm/grovemoisture.hpp
/usr/include/upm/groveo2.hpp
/usr/include/upm/groverelay.hpp
/usr/include/upm/groverotary.hpp
/usr/include/upm/grovescam.hpp
/usr/include/upm/groveslide.hpp
/usr/include/upm/grovespeaker.hpp
/usr/include/upm/grovetemp.hpp
/usr/include/upm/groveultrasonic.hpp
/usr/include/upm/grovevdiv.hpp
/usr/include/upm/grovewater.hpp
/usr/include/upm/grovewfs.hpp
/usr/include/upm/guvas12d.hpp
/usr/include/upm/h3lis331dl.hpp
/usr/include/upm/hal_aci_tl.h
/usr/include/upm/hcsr04.hpp
/usr/include/upm/hdxxvxta.hpp
/usr/include/upm/hlg150h.hpp
/usr/include/upm/hm11.hpp
/usr/include/upm/hmc5883l.hpp
/usr/include/upm/hmtrp.hpp
/usr/include/upm/hp20x.hpp
/usr/include/upm/ht9170.hpp
/usr/include/upm/htu21d.hpp
/usr/include/upm/hx711.hpp
/usr/include/upm/iADC.hpp
/usr/include/upm/iCO2Sensor.hpp
/usr/include/upm/iHumiditySensor.hpp
/usr/include/upm/iLightController.hpp
/usr/include/upm/iLightSensor.hpp
/usr/include/upm/iModuleStatus.hpp
/usr/include/upm/iPressureSensor.hpp
/usr/include/upm/iTemperatureSensor.hpp
/usr/include/upm/ili9341.hpp
/usr/include/upm/ili9341_gfx.hpp
/usr/include/upm/ina132.hpp
/usr/include/upm/isd1820.hpp
/usr/include/upm/itg3200.hpp
/usr/include/upm/jhd1313m1.hpp
/usr/include/upm/joystick12.hpp
/usr/include/upm/kxcjk1013.hpp
/usr/include/upm/l298.hpp
/usr/include/upm/l3gd20.hpp
/usr/include/upm/lcd.hpp
/usr/include/upm/lcm1602.hpp
/usr/include/upm/ldt0028.hpp
/usr/include/upm/lib_aci.h
/usr/include/upm/lm35.hpp
/usr/include/upm/lol.hpp
/usr/include/upm/loudness.hpp
/usr/include/upm/lp8860.hpp
/usr/include/upm/lpd8806.hpp
/usr/include/upm/lsm303.hpp
/usr/include/upm/lsm9ds0.hpp
/usr/include/upm/m24lr64e.hpp
/usr/include/upm/max31723.hpp
/usr/include/upm/max31855.hpp
/usr/include/upm/max44000.hpp
/usr/include/upm/max44009.hpp
/usr/include/upm/max5487.hpp
/usr/include/upm/maxds3231m.hpp
/usr/include/upm/maxsonarez.hpp
/usr/include/upm/mcp9808.hpp
/usr/include/upm/mg811.hpp
/usr/include/upm/mhz16.hpp
/usr/include/upm/mic.hpp
/usr/include/upm/micsv89.hpp
/usr/include/upm/mlx90614.hpp
/usr/include/upm/mma7455.hpp
/usr/include/upm/mma7660.hpp
/usr/include/upm/mpl3115a2.hpp
/usr/include/upm/mpr121.hpp
/usr/include/upm/mpu60x0.hpp
/usr/include/upm/mpu9150.hpp
/usr/include/upm/mpu9250.hpp
/usr/include/upm/mq2.hpp
/usr/include/upm/mq3.hpp
/usr/include/upm/mq303a.hpp
/usr/include/upm/mq4.hpp
/usr/include/upm/mq5.hpp
/usr/include/upm/mq6.hpp
/usr/include/upm/mq7.hpp
/usr/include/upm/mq8.hpp
/usr/include/upm/mq9.hpp
/usr/include/upm/ms5611.hpp
/usr/include/upm/my9221.hpp
/usr/include/upm/nlgpio16.hpp
/usr/include/upm/nrf24l01.hpp
/usr/include/upm/nrf8001.hpp
/usr/include/upm/nunchuck.hpp
/usr/include/upm/otp538u.hpp
/usr/include/upm/pca9685.hpp
/usr/include/upm/pn532.hpp
/usr/include/upm/ppd42ns.hpp
/usr/include/upm/pulsensor.hpp
/usr/include/upm/rfr359f.hpp
/usr/include/upm/rgbringcoder.hpp
/usr/include/upm/rhusb.hpp
/usr/include/upm/rotaryencoder.hpp
/usr/include/upm/rpr220.hpp
/usr/include/upm/sainsmartks.hpp
/usr/include/upm/servo.hpp
/usr/include/upm/si1132.hpp
/usr/include/upm/si114x.hpp
/usr/include/upm/si7005.hpp
/usr/include/upm/sm130.hpp
/usr/include/upm/smartdrive.hpp
/usr/include/upm/ssd.hpp
/usr/include/upm/ssd1306.hpp
/usr/include/upm/ssd1308.hpp
/usr/include/upm/ssd1327.hpp
/usr/include/upm/ssd1351.hpp
/usr/include/upm/ssd1351_gfx.hpp
/usr/include/upm/st7735.hpp
/usr/include/upm/st7735_gfx.hpp
/usr/include/upm/stepmotor.hpp
/usr/include/upm/sx1276.hpp
/usr/include/upm/sx6119.hpp
/usr/include/upm/t6713.hpp
/usr/include/upm/ta12200.hpp
/usr/include/upm/tcs3414cs.hpp
/usr/include/upm/teams.hpp
/usr/include/upm/tex00.hpp
/usr/include/upm/th02.hpp
/usr/include/upm/tm1637.hpp
/usr/include/upm/tp401.hpp
/usr/include/upm/tsl2561.hpp
/usr/include/upm/ttp223.hpp
/usr/include/upm/ublox6.hpp
/usr/include/upm/uln200xa.hpp
/usr/include/upm/urm37.hpp
/usr/include/upm/vcap.hpp
/usr/include/upm/waterlevel.hpp
/usr/include/upm/wheelencoder.hpp
/usr/include/upm/wt5001.hpp
/usr/include/upm/xbee.hpp
/usr/include/upm/yg1006.hpp
/usr/include/upm/zfm20.hpp
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files python
%defattr(-,root,root,-)
/usr/lib64/python*/*
