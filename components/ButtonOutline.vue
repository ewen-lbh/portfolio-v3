<template lang="pug">
    button(:name="name", :id="name ? `btn--${name}` : false"): slot
</template>

<script>
export default {
  name: 'ButtonOutline',
  props: {
    name: {
      type: [String, Boolean],
      default: false
    }
  }
}
</script>

<style lang="stylus" scoped>
button {
  box-shadow: none;
  background: transparent;
  border: 2px solid white;
  border-radius: 0;
  padding: 10px 20px;
  color: white;
  font-family: 'Narita Monospace';
  font-size: 20px;
  // ---------------------------------------------------
  transition: all 0.25s ease;
}

button:hover {
  background: white;
  color: black;
  cursor: pointer;
}
</style>
