import React from 'react';
import {
    StyleSheet,
    View,
    Text,
    TextInput,
    TouchableOpacity,
    SafeAreaView,
} from 'react-native';

const CreateAccount = ({ navigation }) => {
    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.content}>
                <Text style={styles.title}>Create account!</Text>
                
                <View style={styles.inputContainer}>
                    <Text style={styles.label}>Name</Text>
                    <TextInput
                        style={styles.input}
                        placeholder=""
                    />
                    
                    <Text style={styles.label}>Email</Text>
                    <TextInput
                        style={styles.input}
                        placeholder=""
                        keyboardType="email-address"
                    />
                    
                    <Text style={styles.label}>Password</Text>
                    <TextInput
                        style={styles.input}
                        placeholder=""
                        secureTextEntry
                    />
                </View>

                <TouchableOpacity 
                    style={styles.button}
                    onPress={() => navigation.navigate('Verification')} //Anasayfayı entegre edince buraya anasayfa gelecek!!!
                >
                    <Text style={styles.buttonText}>Sign Up</Text>
                </TouchableOpacity>

                <View style={styles.footer}>
                    <Text style={styles.footerText}>Already have an account?</Text>
                    <TouchableOpacity onPress={() => navigation.navigate('Login')}>
                        <Text style={styles.loginText}>Log in</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </SafeAreaView>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#5CCBF0',
    },
    content: {
        flex: 1,
        padding: 20,
        paddingTop: 60,
    },
    title: {
        fontSize: 32,
        color: 'white',
        marginBottom: 40,
    },
    inputContainer: {
        marginBottom: 30,
    },
    label: {
        color: 'white',
        fontSize: 16,
        marginBottom: 8,
    },
    input: {
        backgroundColor: '#F5F5F5',
        borderRadius: 10,
        padding: 15,
        marginBottom: 20,
        shadowColor: '#000',
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    button: {
        backgroundColor: '#1B2C49',
        padding: 15,
        borderRadius: 25,
        alignItems: 'center',
        marginBottom: 20,
        shadowColor: '#000',
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    buttonText: {
        color: 'white',
        fontSize: 16,
        fontWeight: 'bold',
    },
    footer: {
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'center',
    },
    footerText: {
        color: 'white',
        marginRight: 5,
    },
    loginText: {
        color: 'white',
        fontWeight: 'bold',
    },
});

export default CreateAccount;