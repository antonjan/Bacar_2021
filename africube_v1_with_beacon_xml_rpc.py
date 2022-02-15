#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Test Rpitx
# Author: root
# GNU Radio version: 3.8.2.0

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import rpitx
import soapy
import distutils
from distutils import util
try:
    from xmlrpc.server import SimpleXMLRPCServer
except ImportError:
    from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading


class africube_v1_with_beacon_xml_rpc(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Test Rpitx")

        ##################################################
        # Variables
        ##################################################
        self.tran_tx_freq = tran_tx_freq = 145970000
        self.sdrplay_rx_gain = sdrplay_rx_gain = 10
        self.samp_rate_0 = samp_rate_0 = 1248000
        self.samp_rate = samp_rate = 48000*2
        self.rx_freq = rx_freq = 435100000
        self.lpf_cutoff_freq = lpf_cutoff_freq = 20000
        self.low_pass_filter_gain = low_pass_filter_gain = 1
        self.beacon_tau = beacon_tau = 75e-6
        self.beacon_offset_freq = beacon_offset_freq = -24000
        self.beacon_offset = beacon_offset = 0
        self.beacon_int_phase = beacon_int_phase = 0
        self.beacon_deviation = beacon_deviation = 2.5e3
        self.beacon_Preemphasis = beacon_Preemphasis = -1
        self.SDR_rf_gain = SDR_rf_gain = 1
        self.LPF_rf_gain_0 = LPF_rf_gain_0 = 9
        self.Beacon_mod_gain = Beacon_mod_gain = 0.8
        self.Beacom_overall_gain = Beacom_overall_gain = 0.8
        self.Beacom_mixer_gain = Beacom_mixer_gain = 0.8

        ##################################################
        # Blocks
        ##################################################
        self.xmlrpc_server_0 = SimpleXMLRPCServer(('127.0.0.1', 8008), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.soapy_source_0 = None
        # Make sure that the gain mode is valid
        if('Overall' not in ['Overall', 'Specific', 'Settings Field']):
            raise ValueError("Wrong gain mode on channel 0. Allowed gain modes: "
                  "['Overall', 'Specific', 'Settings Field']")

        dev = 'driver=sdrplay'

        # Stream arguments for every activated stream
        tune_args = ['']
        settings = ['']

        # Setup the device arguments
        dev_args = 'driver=sdrplay'

        self.soapy_source_0 = soapy.source(1, dev, dev_args, '',
                                  tune_args, settings, samp_rate, "fc32")



        self.soapy_source_0.set_dc_removal(0,bool(distutils.util.strtobool('False')))

        # Set up DC offset. If set to (0, 0) internally the source block
        # will handle the case if no DC offset correction is supported
        self.soapy_source_0.set_dc_offset(0,0)

        # Setup IQ Balance. If set to (0, 0) internally the source block
        # will handle the case if no IQ balance correction is supported
        self.soapy_source_0.set_iq_balance(0,0)

        self.soapy_source_0.set_agc(0,False)

        # generic frequency setting should be specified first
        self.soapy_source_0.set_frequency(0, rx_freq)

        self.soapy_source_0.set_frequency(0,"BB",0)

        # Setup Frequency correction. If set to 0 internally the source block
        # will handle the case if no frequency correction is supported
        self.soapy_source_0.set_frequency_correction(0,0)

        self.soapy_source_0.set_antenna(0,'RX')

        self.soapy_source_0.set_bandwidth(0,0)

        if('Overall' != 'Settings Field'):
            # pass is needed, in case the template does not evaluare anything
            pass
            self.soapy_source_0.set_gain(0,SDR_rf_gain)
        self.rpitx_rpitx_source_0 = rpitx.rpitx_source(samp_rate, tran_tx_freq)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                LPF_rf_gain_0,
                samp_rate,
                lpf_cutoff_freq,
                samp_rate/32,
                firdes.WIN_HAMMING,
                6.76))
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(Beacom_overall_gain)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(Beacon_mod_gain)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.band_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                21000,
                30000,
                samp_rate/32,
                firdes.WIN_HAMMING,
                6.76))
        self.audio_source_0 = audio.source(48000, 'hw:2,1', True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, beacon_offset_freq, Beacom_mixer_gain, beacon_offset, beacon_int_phase)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=48000,
        	quad_rate=samp_rate,
        	tau=beacon_tau,
        	max_dev=beacon_deviation,
        	fh=beacon_Preemphasis,
                )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.audio_source_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.rpitx_rpitx_source_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.soapy_source_0, 0), (self.low_pass_filter_0, 0))


    def get_tran_tx_freq(self):
        return self.tran_tx_freq

    def set_tran_tx_freq(self, tran_tx_freq):
        self.tran_tx_freq = tran_tx_freq
        self.rpitx_rpitx_source_0.set_freq(self.tran_tx_freq)

    def get_sdrplay_rx_gain(self):
        return self.sdrplay_rx_gain

    def set_sdrplay_rx_gain(self, sdrplay_rx_gain):
        self.sdrplay_rx_gain = sdrplay_rx_gain

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 21000, 30000, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.LPF_rf_gain_0, self.samp_rate, self.lpf_cutoff_freq, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.soapy_source_0.set_frequency(0, self.rx_freq)

    def get_lpf_cutoff_freq(self):
        return self.lpf_cutoff_freq

    def set_lpf_cutoff_freq(self, lpf_cutoff_freq):
        self.lpf_cutoff_freq = lpf_cutoff_freq
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.LPF_rf_gain_0, self.samp_rate, self.lpf_cutoff_freq, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))

    def get_low_pass_filter_gain(self):
        return self.low_pass_filter_gain

    def set_low_pass_filter_gain(self, low_pass_filter_gain):
        self.low_pass_filter_gain = low_pass_filter_gain

    def get_beacon_tau(self):
        return self.beacon_tau

    def set_beacon_tau(self, beacon_tau):
        self.beacon_tau = beacon_tau

    def get_beacon_offset_freq(self):
        return self.beacon_offset_freq

    def set_beacon_offset_freq(self, beacon_offset_freq):
        self.beacon_offset_freq = beacon_offset_freq
        self.analog_sig_source_x_0.set_frequency(self.beacon_offset_freq)

    def get_beacon_offset(self):
        return self.beacon_offset

    def set_beacon_offset(self, beacon_offset):
        self.beacon_offset = beacon_offset
        self.analog_sig_source_x_0.set_offset(self.beacon_offset)

    def get_beacon_int_phase(self):
        return self.beacon_int_phase

    def set_beacon_int_phase(self, beacon_int_phase):
        self.beacon_int_phase = beacon_int_phase
        self.analog_sig_source_x_0.set_phase(self.beacon_int_phase)

    def get_beacon_deviation(self):
        return self.beacon_deviation

    def set_beacon_deviation(self, beacon_deviation):
        self.beacon_deviation = beacon_deviation
        self.analog_nbfm_tx_0.set_max_deviation(self.beacon_deviation)

    def get_beacon_Preemphasis(self):
        return self.beacon_Preemphasis

    def set_beacon_Preemphasis(self, beacon_Preemphasis):
        self.beacon_Preemphasis = beacon_Preemphasis

    def get_SDR_rf_gain(self):
        return self.SDR_rf_gain

    def set_SDR_rf_gain(self, SDR_rf_gain):
        self.SDR_rf_gain = SDR_rf_gain
        self.soapy_source_0.set_gain(0, self.SDR_rf_gain)

    def get_LPF_rf_gain_0(self):
        return self.LPF_rf_gain_0

    def set_LPF_rf_gain_0(self, LPF_rf_gain_0):
        self.LPF_rf_gain_0 = LPF_rf_gain_0
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.LPF_rf_gain_0, self.samp_rate, self.lpf_cutoff_freq, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))

    def get_Beacon_mod_gain(self):
        return self.Beacon_mod_gain

    def set_Beacon_mod_gain(self, Beacon_mod_gain):
        self.Beacon_mod_gain = Beacon_mod_gain
        self.blocks_multiply_const_vxx_0.set_k(self.Beacon_mod_gain)

    def get_Beacom_overall_gain(self):
        return self.Beacom_overall_gain

    def set_Beacom_overall_gain(self, Beacom_overall_gain):
        self.Beacom_overall_gain = Beacom_overall_gain
        self.blocks_multiply_const_vxx_0_0.set_k(self.Beacom_overall_gain)

    def get_Beacom_mixer_gain(self):
        return self.Beacom_mixer_gain

    def set_Beacom_mixer_gain(self, Beacom_mixer_gain):
        self.Beacom_mixer_gain = Beacom_mixer_gain
        self.analog_sig_source_x_0.set_amplitude(self.Beacom_mixer_gain)





def main(top_block_cls=africube_v1_with_beacon_xml_rpc, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
