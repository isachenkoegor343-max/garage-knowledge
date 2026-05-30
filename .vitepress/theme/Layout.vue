<template>
  <DefaultTheme.Layout>
    <template #layout-bottom>
      <ChatWidget />
    </template>
  </DefaultTheme.Layout>
</template>

<script setup>
import DefaultTheme from 'vitepress/theme'
import ChatWidget from './ChatWidget.vue'
</script>