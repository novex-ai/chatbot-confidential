<template>
      <div style="width: 100%; max-width: 400px">
        <q-chat-message
          label="Sunday, 19th"
        />
  
        <q-chat-message
          :text="['hey, how are you?']"
          sent
          stamp="7 minutes ago"
        />
        <q-chat-message
          :text="['doing fine, how are you?']"
          stamp="4 minutes ago"
        />
      </div>
  </template>
