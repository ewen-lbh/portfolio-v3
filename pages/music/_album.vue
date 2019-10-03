<template lang="pug">
    #inner-content
        h1 {{album}}
</template>

<script>
export default {
  data() {
    return {
      album: this.$route.params.album
        .replace(/-/g, ' ')
        .split(' ')
        .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
        .join(' ')
    }
  }
}
</script>

<style lang="stylus" scoped>
h1 {
  text-transform: title;
}
</style>
