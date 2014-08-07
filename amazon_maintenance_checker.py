__author__ = 'apeckys'

import boto.ec2
from boto.ec2 import instancestatus, instanceinfo


def __main():
  regions = ['us-east-1', 'us-west-1', 'us-west-2', 'eu-west-1', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1',
             'sa-east-1']
  headers = ['Name', 'instance.id', 'instance.zone', 'instance.events.code', 'instance.events.description',
             'instance.events.not_before', 'instance.events.not_after']
  print '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(headers)

  for region in regions:

    conn = boto.ec2.connect_to_region(region)
    stats = conn.get_all_instance_status()

    for instance in stats:
      if instance.events:
        foo = conn.get_all_instances(instance_ids=instance.id)

        print '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(foo[0].instances[0].tags['Name'], instance.id, instance.zone,
                                                  instance.events[0].code, instance.events[0].description,
                                                  instance.events[0].not_before, instance.events[0].not_after)


# This is the conventional entry point for the start of the main script
if __name__ == '__main__':
  __main()

