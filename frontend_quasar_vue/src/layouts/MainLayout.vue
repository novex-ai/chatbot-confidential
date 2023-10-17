<template>
  <q-layout view="hHh lpr fFf">
    <q-header elevated>
      <q-toolbar class="shadow-2">
        <q-tabs>
          <q-route-tab to="/" label="Chat" />
          <q-route-tab to="/data" label="Data" />
        </q-tabs>

        <q-space />

        <q-tabs>
          <q-route-tab to="/settings" label="Settings" />
        </q-tabs>
      </q-toolbar>
    </q-header>

    <q-page-container
      class="row items-start justify-evenly q-ma-lg"
    >
      <router-view class="app-page" />
    </q-page-container>

    <q-footer reveal elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-space />
        <div>
          chatbot-confidential
        </div>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<style lang="scss">
.app-page {
  width: 100%;
  max-width: 600px;
}
</style>