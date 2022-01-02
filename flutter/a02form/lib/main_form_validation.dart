import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Flutter Demo',
      home: FormScreen(title: 'Flutter Form Validation'),
    );
  }
}

class FormScreen extends StatefulWidget {
  const FormScreen({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  State<FormScreen> createState() => _FormScreenState();
}

class _FormScreenState extends State<FormScreen> {
  // Create a global key that uniquely identifies the Form widget and allows validation of the form.
  // Note: This is a GlobalKey<FormState>, not a GlobalKey<MyCustomFormState>.
  final _formKey = GlobalKey<FormState>();

  String _id = '';
  String _password = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Form(
        key: _formKey,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Padding(
                padding: const EdgeInsets.all(20),
                child: Column(
                  children: [
                    const Text(
                      'name',
                      style: TextStyle(
                        fontSize: 25.0,
                      ),
                    ),
                    TextFormField(
                      // inputFormatters: [FilteringTextInputFormatter(RegExp('[0-9]'), allow:false), ],
                      autovalidateMode: AutovalidateMode.always,

                      decoration: const InputDecoration(
                        icon: Icon(Icons.person),
                        hintText: 'Hint Text',
                        labelText: 'Label Text',
                      ),

                      onSaved: (value) {
                        setState(() {
                          _id = value as String;
                        });
                      },
                      validator: (value) {
                        if (value == null || value.isEmpty) {
                          return 'Please enter some text';
                        }
                        return null;
                      },
                    ),
                  ],
                )),
            Padding(
                padding: const EdgeInsets.fromLTRB(20, 20, 20, 20),
                child: Column(
                  children: [
                    const Text(
                      'password',
                      style: TextStyle(
                        fontSize: 25.0,
                      ),
                    ),
                    TextFormField(
                        autovalidateMode: AutovalidateMode.always,
                        onSaved: (value) {
                          setState(() {
                            _password = value as String;
                          });
                        },
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter some text';
                          }
                          if (value.toString().length < 8) {
                            return '8자 이상 입력';
                          }
                          if (!RegExp('[0-9]').hasMatch(value)) {
                            return '정규식';
                          }
                          return null;
                        }
                        // focusNode: _passwordFocusNode,
                        // keyboardType: TextInputType.text ,
                        // obscureText: true,
                        // decoration: InputDecoration(
                        //   labelText: "비밀번호",
                        //   suffixIcon: Icon(Icons.lock),
                        // ),
                        // textInputAction: TextInputAction.done,
                        ),

                    // SizedBox( height: 16, ),

                    ElevatedButton(
                      onPressed: () {
                        // Validate returns true if the form is valid, or false otherwise.
                        if (_formKey.currentState!.validate()) {
                          // validation 이 성공하면 폼 저장하기
                          _formKey.currentState!.save();

                          // If the form is valid, display a SnackBar. In the real world,
                          // you'd often call a server or save the information in a database.
                          ScaffoldMessenger.of(context).showSnackBar(
                            SnackBar(content: Text(_id + '/' + _password)),
                          );
                        }
                      },
                      child: const Text('Submit'),
                    ),
                  ],
                )),
          ],
        ),
      ),
    );
  }
}
