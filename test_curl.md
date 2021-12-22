* Obtain access token for user in the realm master with username admin and password password:
```sh
curl \
  -d "client_id=admin-cli" \
  -d "username=keycloak" \
  -d "password=keycloak" \
  -d "grant_type=password" \
  "http://localhost:28080/auth/realms/master/protocol/openid-connect/token" | jq
```

* get detials of master realm:
```sh
curl \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJYTnNYd0dYXzliVFZyLVlLUkxIVHpSaFA3dVhwNUJ2aTl3a210UkZMakJvIn0.eyJleHAiOjE2NDAxOTYyNzMsImlhdCI6MTY0MDE5NjIxMywianRpIjoiZWY3NDVjNWMtYWJlMC00NTljLWE3MjctZDFkMDg2YWE2NzhhIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDoyODA4MC9hdXRoL3JlYWxtcy9tYXN0ZXIiLCJzdWIiOiIyNzY2ZDZlYi1lZGMwLTRjMWYtOTA5MC0wNDE4M2I3NWZhNTUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJhZG1pbi1jbGkiLCJzZXNzaW9uX3N0YXRlIjoiZGM3NzgyMDgtYWI5Ny00ZjI4LTk3NTktMzdmMDg2NTYyYjNiIiwiYWNyIjoiMSIsInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoia2V5Y2xvYWsifQ.IX_VEYGyTB2svk4fpjmOTiyKBzVxnS08f5OAHAk_fUSSZ42c1iZTBbSgcZtLsW4Gb39gQqXj0jLvy_BAXayE9rFRQQptimCtfpdBi_07gL1AGrcrh20IUBkwZq12WuDY8rp8kJ1pe1nvJzUuBn-CpD7ee-vs53JwLW_aSUzvolEX-6Y0Qt-jZ6NurVBY3-fjtqfFqKbYyWqGHlF_ZA9UNToTiw3lurnx7Kt9swigizpflpXw1cZSJPWFHD53gFz1FW5iKQYEuVf3Bc3dT70ZfKwnBFtg7zhvsbzbTUT-nqWjP20RpGT3Uu_a-teN-6c1TRcaNPpoigrZXapm-A6Uyw" \
  "http://localhost:28080/auth/admin/realms/master" | jq
```

