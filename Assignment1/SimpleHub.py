from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr

log = core.getLogger()

def _handle_ConnectionUp (event):
  msg = of.ofp_flow_mod()
  msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
  event.connection.send(msg)
  log.info("Hubifying %s", dpidToStr(event.dpid))

def launch ():
  core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)

  log.info("Hub running.")

#ofp_flow_mod is a class that helps in modifying flow tables. This is the class:
#class ofp_flow_mod (ofp_header):
#  def __init__ (self, **kw):
#    ofp_header.__init__(self)
#    self.header_type = OFPT_FLOW_MOD
#    if 'match' in kw:
#      self.match = None
#    else:
#      self.match = ofp_match()
#    self.cookie = 0
#    self.command = OFPFC_ADD
#    self.idle_timeout = OFP_FLOW_PERMANENT
#    self.hard_timeout = OFP_FLOW_PERMANENT
#    self.priority = OFP_DEFAULT_PRIORITY
#    self.buffer_id = None
#    self.out_port = OFPP_NONE
#    self.flags = 0
#    self.actions = []
