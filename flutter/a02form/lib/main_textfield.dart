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
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                children: [
                  TextFormField(
                    decoration: const InputDecoration(
                      icon: Icon(Icons.person),
                      prefixIcon: Icon(Icons.phone),
                      suffixIcon: Icon(Icons.star),
                      hintText: 'Hint Text',
                      labelText: 'Label Text',
                      prefixText: 'PrefixText',
                      suffixText: 'suffixtext',
                    ),
                  ),
                  Padding(padding:  const EdgeInsets.fromLTRB(0, 0, 0, 20),),

                  TextFormField(
                    decoration: const InputDecoration(
                      icon: Icon(Icons.person),
                      prefixIcon: Icon(Icons.phone),
                      suffixIcon: Icon(Icons.star),
                      hintText: 'Hint Text',
                      labelText: 'Label Text',
                      prefixText: 'PrefixText',
                      suffixText: 'Suffixtext',
                    ),
                  ),

                  Padding(padding:  const EdgeInsets.fromLTRB(0, 0, 0, 20),),

                  TextFormField(
                    decoration: const InputDecoration(
                      icon: Icon(Icons.person),
                      prefixIcon: Icon(Icons.phone),
                      suffixIcon: Icon(Icons.star),
                      hintText: 'Hint Text',
                      labelText: 'Label Text',
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(20)),
                        borderSide: BorderSide(
                          color: Colors.blue,
                        ),
                      ),
                    ),
                  ),

                  Padding(padding:  const EdgeInsets.fromLTRB(0, 0, 0, 20),),
                  TextFormField(
                    decoration: const InputDecoration(
                      icon: Icon(Icons.person),
                      prefixIcon: Icon(Icons.phone),
                      suffixIcon: Icon(Icons.star),
                      hintText: 'Hint Text',
                      labelText: 'Label Text',
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(20)),
                        borderSide: BorderSide(
                          color: Colors.blue,
                        ),
                      ),
                      filled: true,
                      fillColor: Colors.amberAccent,
                    ),
                  ),
                ],
              )),
        ],
      ),
    );
  }
}
