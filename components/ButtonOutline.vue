<template lang="pug">
    button(:name="name", :id="name ? `btn--${name}` : false")
      nuxt-link(:to="to" v-if="to")
        slot
      template(v-else)
        slot
</template>

<script>
export default {
  name: 'ButtonOutline',
  props: {
    name: {
      type: [String, Boolean],
      default: false
    },
    to: {
      type: [String, Boolean],
      default: ''
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
  &, a {
    color: white;
    text-decoration none
  }
  font-family: 'Narita Monospace';
  font-size: 20px;
  // ---------------------------------------------------
  transition: all 0.125s ease;
}

button:hover {
  background: white;
  color: black;
  cursor: pointer;
  a {
    color black
  }
}
</style>
