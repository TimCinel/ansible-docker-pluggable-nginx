import os

def basename(path):
  return path.split(os.sep)[-1]

def ssl_list(ssl_items, src_dir, dest_dir):
  return map(lambda ssl_item: "%s/%s:%s/%s" % (src_dir, ssl_item['dest_name'], dest_dir, ssl_item['dest_name']), ssl_items)

def config_list(config_items, src_dir):
  return map(lambda config_item: "%s/%s:%s" % (src_dir, basename(config_item['src']), config_item['dest']), config_items)

class FilterModule(object):
  def filters(self):
    return {
      'ssl_list': ssl_list,
      'config_list': config_list,
    }
