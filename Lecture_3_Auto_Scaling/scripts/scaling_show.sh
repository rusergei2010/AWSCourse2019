#! /bin/bash

URL=$1

function get_instance_id_from_elb_url(){
  local elb_url="$1"

  curl -s "$elb_url" | grep -o '<p>i-[^<]*' | sed 's@<p>@@'
}

while true; do
  instance_base=$(get_instance_id_from_elb_url $URL)
  sleep 5
  instance_new=$(get_instance_id_from_elb_url $URL)
  if [[ "$instance_base" != "$instance_new" ]]; then
    echo "========>  Scaled !  <=========!"
    echo "=> $(date) $instance_new; $instance_base"
  else
    echo "=> $(date) $instance_base"
  fi
done
