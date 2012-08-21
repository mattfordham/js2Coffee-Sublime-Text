import sublime, sublime_plugin, subprocess, os

class Js2coffeeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    selection = self.view.sel()
    for region in selection:
      region_text = self.view.substr(region)
      pr = subprocess.Popen(['js2coffee'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
      result, stderrdata = pr.communicate(region_text)
      self.view.replace(edit, region, result)