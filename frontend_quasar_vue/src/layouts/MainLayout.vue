<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="shadow-2">
        <q-btn
          stretch
          flat
          to="/"
          label="Chat"
          :class='{"text-light-blue-2": currentRoutePath === "/"}'
        />
        <q-btn
          stretch
          flat
          to="/data"
          label="Data"
          :class='{"text-light-blue-2": currentRoutePath === "/data"}'
        />
        <q-space />
        <q-btn
          stretch
          flat
          to="/settings"
          label="Settings"
          :class='{"text-light-blue-2": currentRoutePath === "/settings"}'
        />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const currentRoutePath = computed(() => route.path);
</script>
