import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Platform, InteractionManager } from 'react-native';
import 'react-native-polyfill-globals';
import { LogBox } from 'react-native';


// Sayfa bileşenlerini içe aktarın
import WelcomeScreen from './mainPage';
import Login from './loginPage';
import ForgotPassword from './forgotPassword';
import CreateNewPassword from './createNewPassword';
import VerificationCode from './verification';
import PasswordChanged from './passwordChanged';
import CreateAccount from './signUpPage';



const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="WelcomeScreen" screenOptions={{ headerShown: false }}>
        <Stack.Screen name="WelcomeScreen" component={WelcomeScreen} />
        <Stack.Screen name="Login" component={Login} />
        <Stack.Screen name="ForgotPassword" component={ForgotPassword} />
        <Stack.Screen name="CreateNewPassword" component={CreateNewPassword} />
        <Stack.Screen name="Verification" component={VerificationCode} />
        <Stack.Screen name="PasswordChanged" component={PasswordChanged} />
        <Stack.Screen name="SignUp" component={CreateAccount} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
