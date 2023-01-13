
exec(open("Modified_data/realtime.py").read())
exec(open("Modified_data/paper_airplane.dr").read())

trick.trick_view_add_auto_load_file("TV_airplane.tv")
trick.stop(15)

#==================================
# Start the variable server client.
#==================================
varServerPort = trick.var_server_get_port()
PlaneDisplay_path = os.environ['HOME'] + "/PlaneDisplay_Rev1.py"
if (os.path.isfile(PlaneDisplay_path)) :
    PlaneDisplay_cmd = PlaneDisplay_path + " " + str(varServerPort) + " &"
    print(PlaneDisplay_cmd)
    os.system( PlaneDisplay_cmd)
else :
    print('Oops! Can\'t find ' + PlaneDisplay_path )
