<template lang="pug">
    aside#sidebar
        slot
</template>

<style lang="stylus" scoped>
#sidebar
    height 100vh
    width: 300px
    position fixed
    background rgba(0,0,0,0.95)
    animation all 0.5s ease
</style>
