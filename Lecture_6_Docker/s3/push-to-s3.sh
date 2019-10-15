#!/usr/bin/env bash
# var1 = origin, var2 = app, var3 = story
REGISTRY="127.0.0.1:5000"

APP=$1
STORY=$2

# change syngenta to your origin to avoid passing it in
ORIGIN=${3:-meggers}

echo "App:$APP"
echo "Story: $STORY"
echo "Origin:$ORIGIN"

APP_BASE="${ORIGIN}/${APP}"

IMG_ID=`docker images | grep -E '^'$APP'.*latest' | awk -e '{print $3}'`

function assert_env() {
  [ -z "$ORIGIN" ] && echo "Missing ORIGIN Name" && exit 1;
  [ -z "$APP" ] && echo "Missing APP Name" && exit 1;
  [ -z "$STORY" ] && echo "Missing Story Number" && exit 1;
}

function assert_img() {
   echo "IMAGE ID: $IMG_ID"
  [ -z "$IMG_ID" ] && echo "Missing Image ID" && exit 1;
}

function assert_container() {
  RUNNING=$(docker inspect -f {{.State.Running}} registry)
  if [[ "$RUNNING" == 'false' ]]
  then
    echo starting registry
    docker start registry
  fi
}

assert_env


assert_img
assert_container

docker tag "$APP" "$REGISTRY/$APP:$STORY" || exit 1
docker push "$REGISTRY/$APP:$STORY" || exit 1