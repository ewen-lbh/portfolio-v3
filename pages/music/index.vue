<template lang="pug">
  #inner-content
    h1 Music  
    ul.items-grid
      li(v-for="albumSlug in albumSlugs")
        nuxt-link(:to="`/music/${albumSlug}/`")
          h2.tooltip {{albumSlug.replace(/-/g, ' ')}}
          img(:src="`/download/music/${albumSlug}/square-cover-art.jpeg`").cover-art
</template>

<script>
export default {
  data() {
    return {
      albumSlugs: [
        'aria-math-remix',
        'circular',
        'codelines',
        'corrupted',
        // 'etymology',
        'industrial',
        'ink',
        'interstellar',
        'legs-to-run-remix',
        'main-theme-remix',
        'malwr',
        'miss-you-remix',
        'morph',
        'mr-blue-sky-remix',
        'neptune',
        'nihon',
        'patterns',
        'serial',
        'stranger-things-remixes',
        'tesseract',
        'unspecial-effects-remix',
        'work'
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
.items-grid {
  margin: 50px 0;
  display: grid;
  grid-row-gap calc(40px - 23px)
  grid-column-gap 40px
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-template-rows: repeat(auto-fill, minmax(200px, 1fr));

  li {
    list-style: none;
    padding: 0;
    width 100%
    height 100%
    overflow hidden
  }

  li:hover {
    .cover-art {
      // opacity: 0.125
      cursor pointer
    }
    .tooltip {
      opacity: 1
    }
  }
}

.cover-art {
  width: 100%;
  height calc(100% - 23px)
}

.items-grid .tooltip {
  font-family 'Narita Monospace'
  font-size: 23px
  z-index: 10
  bottom: 0
  text-align center
  overflow-x hidden
  text-overflow '···'
  white-space nowrap
  width 100%
  font-weight normal
  position relative
  height: 23px
  opacity: 0
  color white
}
</style>
