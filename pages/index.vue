<template lang="pug">
  #content-inner
    img.big-logo(src="~/assets/images/logos/Mx3-Logo-Light-Glitched.gif")
    p
      | Clean and minimalist designs. Focused beauty. Simple yet visually stunning.
      br
      | Creation for digital mediums: music, motion design, UI/UX design, websites, logos,...
      br
      | Always try to make creative work yourself instead of relying on someone else’s.
      br
      | Learn whatever language, tool or software is required to achieve an idea.
    ButtonOutline(to="/about/").learn-more Learn more

</template>

<script>
import ButtonOutline from '~/components/ButtonOutline.vue'
export default {
  components: { ButtonOutline }
}
</script>

<style lang="stylus" scoped>
#content-inner {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;

  p {
    font-family: 'Narita Monospace';
    line-height: 2.1;
    margin-top: 60px;
  }

  .big-logo {
    height: 150px;
    &:not(:hover) {
      filter saturate(0)
    }
  }

  button.learn-more {
    margin-top: 20px
  }
}
</style>

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
