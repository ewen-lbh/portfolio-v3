<template lang="pug">
  #content-inner
    p Hello world
</template>

<style lang="stylus">
.page-is-index {
  #sidebar {
    width: 0;
    transition: width 0.25s ease;
  }

  #content {
    margin-left: 100px;
    width: calc(100vw - 100px);
    background: black;
  }
}
</style>
