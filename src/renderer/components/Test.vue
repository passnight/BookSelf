<template>
  <div>
      <h1>
          tsaaas
      </h1>
  </div>
</template>

<script>
    import SystemInformation from './LandingPage/SystemInformation'
export default {
    name: 'test',
    components: { SystemInformation },
    methods: {
        open (link) {
          this.$electron.shell.openExternal(link)
        }
    }
}
</script>

<style>

</style>